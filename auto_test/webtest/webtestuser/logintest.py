import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('C:\\Users\\l\\PycharmProjects\\untitled1')

from auto_test.base.browseroperation import Browseroperation
from auto_test.base.usebrowser import UseBrowser
from auto_test.util.excel_operation import OperationExcel
from auto_test.webpage.usermanager.loginpage import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login = LoginPage()
        self.bo = Browseroperation(UseBrowser.driver)

    def test_login_username_password_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert = self.bo.get_alert_text()
        self.assertEqual(alert, self.op.get_cell(1, 4))

    def test_login_success(self):
        self.login.login(self.op.get_cell(2,2), self.op.get_cell(2,3))
        test = self.login.get_page_title()
        self.assertEqual(test, self.op.get_cell(2, 4))

    def test_login_error(self):
        self.login.login(self.op.get_cell(3, 2), self.op.get_cell(3, 3))
        test = self.login.get_alert_text()
        self.assertEqual(test, self.op.get_cell(3, 4))

    def test_login_username_null(self):
        self.login.login(self.op.get_cell(4, 2), self.op.get_cell(4, 3))
        test = self.login.get_alert_text()
        self.assertEqual(test, self.op.get_cell(4, 4))

    def test_login_pwd_null (self):
        self.login.login(self.op.get_cell(5, 2), self.op.get_cell(5, 3))
        test = self.login.get_alert_text()
        self.assertEqual(test, self.op.get_cell(5, 4))

    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(testcase)
    # date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Login_auto_test', description='ui_test')
        runner.run(suite)