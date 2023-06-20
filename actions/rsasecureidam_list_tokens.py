# File: rsasecureidam_list_tokens.py
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


class ListTokens(BaseAction):

    def execute(self):
        self._connector.save_progress("In action handler for: {0}".format(self._connector.get_action_identifier()))

        ret_val, tokens = self.utils.list_tokens(self._action_result, self._param)

        if phantom.is_fail(ret_val):
            return self._action_result.get_status()

        # self._action_result.add_data(tokens)
        for token in tokens:
            self._action_result.add_data(token)

        self._action_result.update_summary({"total_tokens": len(tokens)})

        return self._action_result.set_status(phantom.APP_SUCCESS, f"Total tokens: {len(tokens)}")
