from unittest import TestCase

from splunk_connect_for_snmp_traps.manager.os_config_utils import max_allowed_working_threads


class MaxAllowedWorkingThreadsTest(TestCase):
    def test_max_allowed_working_threads_user_wants_too_many_threads(self):
        user_suggested_threads = 1000000
        working_threads = max_allowed_working_threads(user_suggested_threads)
        self.assertTrue(working_threads < user_suggested_threads)

    def test_max_allowed_working_threads_user_wants_only_few_threads(self):
        user_suggested_threads = 1
        working_threads = max_allowed_working_threads(user_suggested_threads)
        self.assertTrue(working_threads == user_suggested_threads)
