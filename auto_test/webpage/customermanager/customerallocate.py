from auto_test.config.crm_log import Crm_log
from auto_test.util.excel_operation import OperationExcel
from auto_test.util.yaml_opreation import YamlOperation
from auto_test.webpage.usermanager.loginpage import LoginPage


class CustomerAllocate:
    def __init__(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.yaml = YamlOperation('../../config/locator.yaml')
        self.lp = LoginPage()
        self.lp.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
        self.log = Crm_log()

    def allocate_customer(self):
        self.log.set_message('change frame', 'info')
        self.lp.bo.change_frame('/html/frameset/frameset/frame[1]')
        self.log.set_message('click button:客户分配', 'info')
        self.lp.bo.click_element('//*[@id="submenu1"]/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/span/a')
        self.lp.bo.change_frame('mainFrame')
        self.log.set_message('click button:分配', 'info')
        self.lp.bo.click_element('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[10]/td[9]/div/span/a')
        self.log.set_message('click button:提交', 'info')
        self.lp.bo.click_element('/html/body/form/table[2]/tbody/tr/td[2]/input')