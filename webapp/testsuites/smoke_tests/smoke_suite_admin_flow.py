import pytest

from webapp.testcases.log_in_log_out import LogInLogOut


@pytest.mark.usefixtures("machine")
class TestSuite:
    def test_admin_logs_in_successfully(self, machine):
        LogInLogOut(machine=machine).test_admin_logs_in_successfully()

    def test_admin_logs_out_successfully(self, machine):
        LogInLogOut(machine=machine).test_admin_logs_out_successfully()
