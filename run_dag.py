import time

from selenium import webdriver

from locator.dag_locator import model_tab, run_dag
from locator.login_locator import login_username, login_password, login_submit

username = 'admin'
password = 'secret'


url = 'http://192.168.0.114/login'
driver_path = '/Users/mac/PycharmProjects/dag_v2_test/driver/chromedriver'

dag_name = 'backing_test'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)
driver.implicitly_wait(10)

username_input = driver.find_element(*login_username)
username_input.send_keys(username)
password_input = driver.find_element(*login_password)
password_input.send_keys(password)

login_submit_btn = driver.find_element(*login_submit)
login_submit_btn.click()
driver.implicitly_wait(10)

model_tab_btn = driver.find_element(*model_tab)
model_tab_btn.click()
driver.implicitly_wait(20)

run_dag_btn = driver.find_element(*run_dag)
run_dag_btn.click()

