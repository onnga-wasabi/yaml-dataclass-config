"""Tests for pytest scenario"""
from yourproduct import CONFIG
# noinspection PyUnresolvedReferences
from yourproduct.pytest_context import yaml_config  # noqa: F401


class TestConfigHandlerPytest:
    """Tests for pytest scenario"""
    @staticmethod
    # pylint: disable=unused-argument
    def test_config_handler_pytest(yaml_config):  # noqa: F811
        """Config file for test should be loaded."""
        assert CONFIG.some_property == 'test value'
