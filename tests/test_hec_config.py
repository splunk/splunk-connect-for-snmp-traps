import os
from unittest import TestCase

from splunk_connect_for_snmp_traps.manager.hec_config import HecConfiguration


class TestHecConfiguration(TestCase):
    def setUp(self):
        env_vars = (HecConfiguration.endpoints_env_variable_name,
                    HecConfiguration.authentication_token_env_variable_name,
                    HecConfiguration.enable_ssl_env_variable_name)
        for env_var in env_vars:
            if os.environ.get(env_var) is not None:
                del os.environ[env_var]

    def test_no_env_variable_defined_for_hec(self):
        self.assertRaises(ValueError, HecConfiguration)

    def test_only_hec_endpoints_defined(self):
        os.environ[HecConfiguration.endpoints_env_variable_name] = 'http://127.0.0.1:8088/services/hec'
        self.assertRaises(ValueError, HecConfiguration)

    def test_hec_endpoints_and_token_defined(self):
        os.environ[HecConfiguration.endpoints_env_variable_name] = 'http://127.0.0.1:8088/services/hec'
        os.environ[HecConfiguration.authentication_token_env_variable_name] = '12345678'
        self.assertRaises(ValueError, HecConfiguration)

    def test_all_environment_variables_defined_multiple_urls(self):
        os.environ[
            HecConfiguration.endpoints_env_variable_name] = 'http://127.0.0.1:8088/services/hec1   ' \
                                                            'http://127.0.0.1:8088/services/hec2 '
        os.environ[HecConfiguration.authentication_token_env_variable_name] = '12345678'
        os.environ[HecConfiguration.enable_ssl_env_variable_name] = 'Yes'

        config = HecConfiguration()
        self.assertEqual(config.get_endpoints(),
                         ['http://127.0.0.1:8088/services/hec1', 'http://127.0.0.1:8088/services/hec2'])
        self.assertEqual(config.get_authentication_token(), '12345678')
        self.assertTrue(config.is_ssl_enabled())

    def test_all_environment_variables_defined_ssl_enabled(self):
        os.environ[HecConfiguration.endpoints_env_variable_name] = 'http://127.0.0.1:8088/services/hec'
        os.environ[HecConfiguration.authentication_token_env_variable_name] = '12345678'
        os.environ[HecConfiguration.enable_ssl_env_variable_name] = 'Yes'

        config = HecConfiguration()
        self.assertEqual(config.get_endpoints(), ['http://127.0.0.1:8088/services/hec'])
        self.assertEqual(config.get_authentication_token(), '12345678')
        self.assertTrue(config.is_ssl_enabled())

    def test_all_environment_variables_defined_ssl_disabled(self):
        os.environ[HecConfiguration.endpoints_env_variable_name] = 'http://127.0.0.1:8088/services/hec'
        os.environ[HecConfiguration.authentication_token_env_variable_name] = '12345678'
        os.environ[HecConfiguration.enable_ssl_env_variable_name] = 'No'

        config = HecConfiguration()
        self.assertEqual(config.get_endpoints(), ['http://127.0.0.1:8088/services/hec'])
        self.assertEqual(config.get_authentication_token(), '12345678')
        self.assertFalse(config.is_ssl_enabled())
