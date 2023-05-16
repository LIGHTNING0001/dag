from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 设置显示等待时间，有问题
    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    # 判断元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True