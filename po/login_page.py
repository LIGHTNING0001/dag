from po.base import BasePage
from time import sleep


host = '192.168.0.192'
port = 50588
username = 'admin'
password = 'secret'


url = 'http://192.168.0.182:52843'


class LoginPage(BasePage):
    """ 登录页面类 """

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self):
        """ 登录 """

        self.driver.get(url)

        self.driver.implicitly_wait(20)

        self.driver.find_element(*login_address).send_keys(host)
        self.driver.find_element(*login_port).send_keys(port)
        self.driver.find_element(*login_username).send_keys(username)
        self.driver.find_element(*login_password).send_keys(password)

        self.driver.find_element(*login_submit).click()

        # # 获取返回信息
        # element = self.wait(Locator.signin_response)
        #
        # return element.text

        sleep(1)

