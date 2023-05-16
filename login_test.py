import pytest

from po import DagManagePage
from po.login_page import LoginPage
from selenium import webdriver

driver_path = '/Users/mac/PycharmProjects/Seacrhing/UI/driver/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)


@pytest.mark.dependency
def test_login():
    LoginPage(driver).sign_in()


# @pytest.mark.depends(depends=["test_login"])
def test_run_dag():
    LoginPage(driver).sign_in()
    dp = DagManagePage(driver)
    dp.select_module()
    driver.implicitly_wait(20)
    dp.run_dag()


