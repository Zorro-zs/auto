import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from auto_test.base.browseroperation import Browseroperation
from auto_test.base.usebrowser import UseBrowser
from auto_test.util.excel_operation import OperationExcel
from auto_test.webpage.customermanager.customerpage import CustomPage


class CustomerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.cp = CustomPage()
        self.bo = Browseroperation(UseBrowser.driver)

    def test_create_customer(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '添加客户用例参数')
        self.cp.customer_add(name = self.op.get_cell(1,4),date = self.op.get_cell(1,6),add_person=self.op.get_cell(1,7),email=self.op.get_cell(1,5))
        self.assertEqual(self.bo.get_alert_text(),self.op.get_cell(1,8))

    def test_update_customer_message(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '修改客户用例参数')
        self.cp.update_customer_message(job = self.op.get_cell(1,4))
        self.assertEqual(self.bo.get_alert_text(),self.op.get_cell(1,5))

    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(CustomerTest)
    suite.addTests(testcase)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/Login_test_report_' + date_now + '_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Customer_auto_test', description='ui_test')
        runner.run(suite)