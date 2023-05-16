from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from locator.dag_locator import model_tab, test_dag, select_logo, look_btn, add_meta_data, meta_data, defualt_category, \
    open_fund, factor, jobtype, embed_formula, ack, open_fund_dag, index_dag, portfolio, index_first, \
    index_factor_second, portfolio_second
from locator.factor_location import abexcess_ret_1m
from locator.login_locator import login_address, login_password, login_username, login_submit

username = 'admin'
password = 'secret'


url = 'http://192.168.194.241:86/login'
driver_path = '/Users/mac/PycharmProjects/dag_v2_test/driver/chromedriver'


def create_dag(dag, n, first, second, item):

    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    time.sleep(8)
    username_input = driver.find_element(*login_username)
    username_input.send_keys(username)
    password_input = driver.find_element(*login_password)
    password_input.send_keys(password)

    login_submit_btn = driver.find_element(*login_submit)
    login_submit_btn.click()

    time.sleep(5)

    model_tab_btn = driver.find_element(*model_tab)
    model_tab_btn.click()

    time.sleep(5)

    select_logo_btn = driver.find_element(*select_logo)
    select_logo_btn.click()

    time.sleep(2)
    test_dag_btn = driver.find_element(*dag)
    test_dag_btn.click()

    look_btn_1 = driver.find_element(*look_btn)
    look_btn_1.click()
    time.sleep(1)

    for i in range(1, n):
        add_meta_data_btn = driver.find_element(*add_meta_data)
        add_meta_data_btn.click()
        time.sleep(1)

        meta_data_input = driver.find_element(*meta_data)
        meta_data_input.click()
        time.sleep(1)

        defualt_category_input = driver.find_element(*defualt_category)
        defualt_category_input.click()
        time.sleep(0.5)
        open_fund_btn = driver.find_element(*first)
        open_fund_btn.click()
        time.sleep(0.5)
        factor_btn = driver.find_element(*second)
        factor_btn.click()
        time.sleep(0.5)
        f_btn = driver.find_element(By.XPATH, item.format(i))
        f_btn.click()
        time.sleep(0.5)
        job_type = driver.find_element(*jobtype)
        job_type.click()
        time.sleep(0.5)
        embed_formula_btn = driver.find_element(*embed_formula)
        embed_formula_btn.click()
        time.sleep(0.5)
        ack_btn = driver.find_element(*ack)
        ack_btn.click()
        time.sleep(2)

        print(i)

    time.sleep(20)


if __name__ == '__main__':
    create_dag(index_dag, 2, index_first, index_factor_second, '/html/body/div[3]/div/div/div/div/ul[4]/li[{}]/div')
    create_dag(portfolio, 2, open_fund, portfolio_second, '/html/body/div[3]/div/div/div/div/ul[4]/li[{}]/div')
    create_dag(open_fund_dag, 1, open_fund, factor, '/html/body/div[3]/div/div/div/div/ul[4]/li[{}]/div')