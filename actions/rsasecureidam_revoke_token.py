# File: rsasecureidam_disable_token.py
#
# Copyright (c) 2023 Splunk Inc.
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

from actions import BaseAction
from rsasecureidam_consts import RSA_TOKEN_REVOKE_MESSAGE


class RevokeToken(BaseAction):

    def execute(self):
        self._connector.save_progress("In action handler for: {0}".format(self._connector.get_action_identifier()))
        # self.token = self._param.get('token')

        ret_val, response, _ = self.utils.disable_token(self._param)

        if phantom.is_fail(ret_val):
            self._action_result.set_status(phantom.APP_ERROR, response)
            return self._action_result.get_status()

        return self._action_result.set_status(phantom.APP_SUCCESS, RSA_TOKEN_REVOKE_MESSAGE)