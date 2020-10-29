from selenium.webdriver.common.alert import Alert


class Browseroperation:
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'element not find')

    def get_text(self,xpath):
        try:
            text = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'element not found')
        return text

    def get_alert_text(self):
        return Alert(self.driver).text

    def change_frame(self,frame_name):
        if '/' not in frame_name:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(frame_name)
        else:
            self.driver.switch_to.parent_frame()
            name = self.driver.find_element_by_xpath(frame_name)
            self.driver.switch_to.frame(name)

    def clear(self,xpath):
        self.driver.find_element_by_xpath(xpath).clear()

    def change_window(self,name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title == name:
                break