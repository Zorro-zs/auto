import unittest

from auto_test.base.browseroperation import Browseroperation
from auto_test.base.usebrowser import UseBrowser
from auto_test.db.customer_db.customeroperdb import CustomerOprationDb
from auto_test.util.excel_operation import OperationExcel
from auto_test.webpage.customermanager.customerallocate import CustomerAllocate


class CustomerAllocateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.ca = CustomerAllocate()
        self.bo = Browseroperation(UseBrowser.driver)
        self.dbop = CustomerOprationDb()

    def test_allocate_customer(self):
        self.ca.allocate_customer()
        text = self.bo.get_alert_text()
        self.assertEqual(text,'客户分配成功')
        self.dbop.update_table_by_id(18)


    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    unittest.main()
