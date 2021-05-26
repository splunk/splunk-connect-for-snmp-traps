#   ########################################################################
#   Copyright 2021 Splunk Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#   ########################################################################
from unittest import TestCase

from splunk_connect_for_snmp_traps.manager.os_config_utils import (
    max_allowed_working_threads,
)


class MaxAllowedWorkingThreadsTest(TestCase):
    def test_max_allowed_working_threads_user_wants_too_many_threads(self):
        user_suggested_threads = 1000000
        working_threads = max_allowed_working_threads(user_suggested_threads)
        self.assertTrue(working_threads < user_suggested_threads)

    def test_max_allowed_working_threads_user_wants_only_few_threads(self):
        user_suggested_threads = 1
        working_threads = max_allowed_working_threads(user_suggested_threads)
        self.assertTrue(working_threads == user_suggested_threads)
