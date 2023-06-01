# File: rsasecureidam_test_connectivity.py
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

import phantom.app as phantom

# import rsasecureidam_consts as consts
from actions import BaseAction


class TestConnectivity(BaseAction):

    def execute(self):
        # self.config = self._connector.get_config(self._action_result)
        # self._connector.save_progress("In action handler for: {0}".format(self._connector.get_action_identifier()))

        ret_val, response, error_message = self._connector.utils._start_connection()

        if phantom.is_fail(ret_val):
            self._action_result.set_status(phantom.APP_ERROR, response)
            self._connector.save_progress("Test Connectivity Failed")
            return self._action_result.get_status(), error_message

        self._connector.save_progress("Test Connectivity Passed")
        return self._action_result.set_status(phantom.APP_SUCCESS), response
