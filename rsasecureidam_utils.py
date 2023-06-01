# File: rsasecureidam_utils.py
#
# Copyright (c) None Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import socket
import time

import paramiko
from bs4 import UnicodeDammit

try:
    from urlparse import urlparse
except Exception:
    from urllib.parse import urlparse

from rsasecureidam_consts import *


class RSASecureIdAMUtils(object):

    def __init__(self, connector):
        self._connector = connector
        self._username = self._connector.config.get("username")
        self._password = self._connector.config.get("password")
        self._endpoint = urlparse(self._connector.config.get("url")).hostname

    def _start_connection(self):

        self._connector.save_progress(f"Connecting to {self._endpoint}")
        user = self._username
        password = self._password

        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self._ssh_client.connect(hostname=self._endpoint, username=user,
                    password=password, allow_agent=False, look_for_keys=True,
                    timeout=30)
        except Exception as e:
            return False, "SSH connection attempt failed. Please enter valid values for 'ssh_username' and 'ssh_password' asset parameters", e

        return True, "SSH connection successful", None

    def _send_command(self, input_data, timeout=0):
        """
           Args:
               command: command to send
               timeout: how long to wait before terminating program
        """
        # attempt to establish connection first
        status, msg, uname_str = self._start_connection()
        if not status:
            return False, msg, uname_str

        try:

            output = ""
            data = ""

            sftp = self._ssh_client.open_sftp()

            filename = int(time.time())
            input_file = "test_{}.csv".format(filename)
            output_file = "test_{}.log".format(filename)
            output_reject_file = "test_rej_{}.csv".format(filename)
            path = "/opt/rsa/am/utils/"
            command = RSA_RUN_COMMAND.format(username=self.super_admin_user, password=self.super_admin_user_password,
                                             input_file=input_file, output_log_file=output_file, output_reject_file=output_reject_file)
            command = RSA_COMMAND_PATH + command

            sftp.chdir(path)
            try:
                f = sftp.file(input_file, 'w', -1)
                f.write(input_data)
                f.close()
            except Exception as e:
                return False, "Error in creating input file. {}".format(e), -1

            trans = self._ssh_client.get_transport()
            self._shell_channel = trans.open_session()
            self._shell_channel.set_combine_stderr(True)

            self._shell_channel.exec_command(command)

            success, data, exit_status = self._get_output(timeout)

            if exit_status:
                if data.find("Error 2004:") != -1:
                    data = str(data).split(":")
                    data = data[1]
                    self._connector.debug_print("Authentication Error.", data)
                else:
                    log_file = sftp.file(output_file, "r")
                    logs = str(log_file.read())
                    if logs.find("Failure") != -1:
                        rej_data_file = sftp.file(output_reject_file, "r")
                        data = rej_data_file.read()
                        self._connector.debug_print(f"Logs for the action: {data}")
                        data = data.splitlines()
                        data = str(data[1]).split(":")
                        data = data[1]
                        rej_data_file.close()
                    self._connector.debug_print("Deleting output files")
                    sftp.remove(output_file)
                    sftp.remove(output_reject_file)

            sftp.remove(input_file)
            output += data

            if (not success):
                return False, f"Could not send command: {command}\r\nOutput: {output}\r\nExit Status: {exit_status}", exit_status
            if exit_status:
                return False, f"Error occured.\r\nOutput: {output}\r\nExit Status: {exit_status}", exit_status
        except Exception as e:
            return False, f"Error sending command:{command}\r\nDetails:{e}", exit_status

        return success, None, exit_status

    def _get_output(self, timeout):
        """
            returns:
                success, data, exit_status
        """
        sendpw = True
        self._shell_channel.settimeout(2)
        self._shell_channel.set_combine_stderr(True)
        output = ""
        stime = int(time.time())

        try:
            while True:
                ctime = int(time.time())
                # data is ready to be received on the channel
                if self._shell_channel.recv_ready():
                    recv_output = UnicodeDammit(self._shell_channel.recv(8000)).unicode_markup
                    if recv_output:
                        output += recv_output
                    else:
                        break

                    # This is pretty messy but it's just the way it is I guess
                    if (sendpw and self._password):
                        try:
                            self._shell_channel.send(f"{self._password}\n")
                        except socket.error:
                            pass
                        sendpw = False
                elif (timeout and ctime - stime >= timeout):
                    return False, "Error: Timeout", None
                elif (self._shell_channel.exit_status_ready() and not self._shell_channel.recv_ready()):
                    break
                time.sleep(1)
        except Exception as e:
            return False, "Error", str(e)

        return True, output, self._shell_channel.recv_exit_status()

    def enable_token(self, param):
        self._connector.debug_print(f"param: {param}")
        token = param["token"]
        self.super_admin_user = param.get("super_admin_user")
        self.super_admin_user_password = param.get("super_admin_user_password")
        data = RSA_HEADER_LINE
        data += RSA_ENABLE_TOKEN_QUERY.format(token=token)
        return self._send_command(data)

    def disable_token(self, param):
        self._connector.debug_print(f"param: {param}")
        token = param["token"]
        self.super_admin_user = param.get("super_admin_user")
        self.super_admin_user_password = param.get("super_admin_user_password")
        data = RSA_HEADER_LINE
        data += RSA_DISABLE_TOKEN_QUERY.format(token=token)
        return self._send_command(data)
