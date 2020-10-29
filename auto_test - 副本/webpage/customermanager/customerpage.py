import time

from auto_test.base.usebrowser import UseBrowser
from auto_test.config.crm_log import Crm_log
from auto_test.util.excel_operation import OperationExcel
from auto_test.util.yaml_opreation import YamlOperation
from auto_test.webpage.usermanager.loginpage import LoginPage


class CustomPage:
    def __init__(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.yaml = YamlOperation('../../config/locator.yaml')
        self.lp = LoginPage()
        self.lp.login(self.op.get_cell(2,2), self.op.get_cell(2,3))
        self.log = Crm_log()

    def customer_add(self,**kwargs):
        self.log.set_message('change frame', 'info')
        self.lp.bo.change_frame(self.yaml.get_locator('SelectCustomer','topframe'))
        self.log.set_message('click button:客户信息', 'info')
        self.lp.bo.click_element(self.yaml.get_locator('SelectCustomer','click_button'))
        self.lp.bo.change_frame(self.yaml.get_locator('CreateCustomer','mainframe'))
        self.lp.bo.click_element(self.yaml.get_locator('CreateCustomer','add_button'))
        time.sleep(2)
        self.log.set_message('click element', 'info')

        self.lp.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_name'),kwargs.get('name',''))
        self.log.set_message('input customer_name:', 'info')
        UseBrowser.driver.execute_script(self.yaml.get_locator('CreateCustomer', 'close_readonly'))
        self.lp.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_birthday'),kwargs.get('date', ''))
        self.log.set_message('input custome_birthday:', 'info')
        self.lp.bo.send_keys(self.yaml.get_locator('CreateCustomer','create_manager'),kwargs.get('add_person', ''))
        self.log.set_message('input option_manager:', 'info')
        self.lp.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_email'),kwargs.get('email', ''))
        self.log.set_message('input customer_email:', 'info')

        time.sleep(4)
        self.lp.bo.click_element(self.yaml.get_locator('CreateCustomer','sure_button'))
        self.log.set_message('create_customer finish', 'info')

    def update_customer_message(self,**kwargs):
        self.log.set_message('change frame', 'info')
        self.lp.bo.change_frame(self.yaml.get_locator('SelectCustomer', 'topframe'))
        self.log.set_message('click button:客户信息', 'info')
        self.lp.bo.click_element(self.yaml.get_locator('SelectCustomer', 'click_button'))
        self.lp.bo.change_frame(self.yaml.get_locator('CreateCustomer', 'mainframe'))
        self.log.set_message('click update', 'info')
        self.lp.bo.click_element(self.yaml.get_locator('UpdateCustomer','update_button'))
        time.sleep(2)
        self.log.set_message('input customerJob :', 'info')
        self.lp.bo.clear(self.yaml.get_locator('UpdateCustomer','customerjob'))
        self.lp.bo.send_keys(self.yaml.get_locator('UpdateCustomer','customerjob'),kwargs.get('job', ''))
        self.log.set_message('click submit', 'info')
        self.lp.bo.click_element(self.yaml.get_locator('UpdateCustomer','submit_button'))



