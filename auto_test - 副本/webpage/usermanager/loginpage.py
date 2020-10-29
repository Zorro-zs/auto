
import time


from selenium.webdriver.common.alert import Alert

from auto_test.base.browseroperation import Browseroperation
from auto_test.base.usebrowser import UseBrowser
from auto_test.config.crm_log import Crm_log
from auto_test.util.excel_operation import OperationExcel
from auto_test.util.yaml_opreation import YamlOperation


class LoginPage:
    def __init__(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.ub = UseBrowser()
        self.bo = Browseroperation(UseBrowser.driver)
        self.yaml = YamlOperation('../../config/locator.yaml')
        self.bo.open_url(self.op.get_cell(1,1))
        self.log = Crm_log()

    def login(self,username='',password=''):
        self.log.set_message('-' * 5 + '登录功能开始', 'info')
        self.bo.send_keys(self.yaml.get_locator('LoginPage','username'),username)
        self.log.set_message('-' * 5 + '输入用户名：' + username, 'info')
        self.bo.send_keys(self.yaml.get_locator('LoginPage','password'),password)
        self.log.set_message('-' * 5 + '输入密码：' + password, 'info')
        self.bo.click_element(self.yaml.get_locator('LoginPage','submit_button'))
        self.log.set_message('-' * 5 + '点击登录', 'info')
        time.sleep(2)

    def get_alert_text(self):
        return Alert(UseBrowser.driver).text

    def get_page_title(self):
        return UseBrowser.driver.title



    def login_correct_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)
        return self.bo.get_text(xpath)