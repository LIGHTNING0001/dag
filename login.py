import math

import pandas as pd
from selenium import webdriver
import time
import pyperclip

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from locator.dag_locator import *
from locator.login_locator import login_address, login_password, login_username, login_submit

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行

import re
import xlrd

username = 'admin'
password = 'secret'

url = 'http://192.168.0.114/login'
driver_path = '/Users/mac/PycharmProjects/dag_v2_test/driver/chromedriver'

dag_name = 'sparse'

df = pd.read_excel('cluster_factor_v2.xlsx')

items = []
n = len(df)

for row in df.iterrows():
    line = []
    line.append(row[1]['name'])
    line.append(row[1]['code'])
    line.append(row[1]['formula'])
    line.append(str(row[1]['timeUnit']))
    items.append(line)

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)


def read_csv():
    factors = []
    with open('cluster_factor.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            t = re.split(',', line)
            print(t)
            # tmp = []
            # tmp.append(t[2])
            # tmp.append(t[3])
            # tmp.append(t[4])
            # factors.append(tmp)

    return factors


def sign_in():

    driver.implicitly_wait(10)

    username_input = driver.find_element(*login_username)
    username_input.send_keys(username)
    password_input = driver.find_element(*login_password)
    password_input.send_keys(password)

    login_submit_btn = driver.find_element(*login_submit)
    login_submit_btn.click()


def add_data_meta():

    time.sleep(10)

    model_tab_btn = driver.find_element(*model_tab)
    model_tab_btn.click()
    driver.implicitly_wait(20)

    create_dag_btn = driver.find_element(*create_dag_item)
    create_dag_btn.click()
    driver.implicitly_wait(20)

    dag_name_input = driver.find_element(*dag_name_ipt)
    dag_name_input.send_keys(dag_name)
    driver.implicitly_wait(20)

    ack_dag_btn = driver.find_element(*ack_dag)
    ack_dag_btn.click()
    #
    # select_logo_btn = driver.find_element(*select_logo)
    # select_logo_btn.click()
    # driver.implicitly_wait(10)
    #
    # test_dag_btn = driver.find_element(*(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div/div[7]/div/div/span[1]'))
    # test_dag_btn.click()
    # driver.implicitly_wait(10)

    time.sleep(1)

    look_btn_1 = driver.find_element(*look_btn)
    look_btn_1.click()
    driver.implicitly_wait(10)
    # 新建元数据节点

    add_meta_data_btn = driver.find_element(*add_meta_data)
    add_meta_data_btn.click()
    time.sleep(1)

    for i in range(18, n):

        print(items[i][0])

        if items[i][3] == 'nan':
            continue

        driver.implicitly_wait(10)

        new_meta_data_btn = driver.find_element(*new_meta_data)
        new_meta_data_btn.click()

        driver.implicitly_wait(10)

        namespace = driver.find_element(*namespace_input)
        namespace.click()
        driver.implicitly_wait(10)

        default = driver.find_element(*default_category)
        default.click()
        driver.implicitly_wait(10)

        stock_item = driver.find_element(*stock_tab)
        stock_item.click()
        driver.implicitly_wait(10)

        stock_factor_item = driver.find_element(*stock_factor)
        stock_factor_item.click()
        driver.implicitly_wait(10)

        physical_table_item = driver.find_element(*physical_table)
        physical_table_item.click()
        driver.implicitly_wait(10)

        barbeyond_store_item = driver.find_element(*barbeyond_store)
        barbeyond_store_item.click()
        driver.implicitly_wait(10)

        if items[i][3] == 'nan':
            stock_daily_factor_item = driver.find_element(*stock_daily_factor)
            stock_daily_factor_item.click()
            driver.implicitly_wait(10)
        elif items[i][3] == 'EMD':
            stock_month_factor_item = driver.find_element(*stock_month_factor)
            stock_month_factor_item.click()
            driver.implicitly_wait(10)
        elif items[i][3] == 'EYD':
            stock_year_factor_item = driver.find_element(*stock_year_factor)
            stock_year_factor_item.click()
            driver.implicitly_wait(10)

        saveDagForm_name_input = driver.find_element(*saveDagForm_name)
        saveDagForm_name_input.send_keys(items[i][0])
        driver.implicitly_wait(10)

        saveDagForm_code_input = driver.find_element(*saveDagForm_code)
        saveDagForm_code_input.send_keys(items[i][1])
        driver.implicitly_wait(10)

        formula_input = driver.find_element(*formula)
        my_action = ActionChains(driver).send_keys_to_element(formula_input, items[i][2]).perform()
        driver.implicitly_wait(10)

        time.sleep(1)

        submit_btn_input = driver.find_element(*submit_btn)
        submit_btn_input.click()

        time.sleep(2)


def create_dag():

    time.sleep(1)

    driver.implicitly_wait(20)
    model_tab_btn = driver.find_element(*model_tab)
    model_tab_btn.click()
    time.sleep(20)

    create_dag_btn = driver.find_element(*create_dag_item)
    create_dag_btn.click()
    driver.implicitly_wait(10)

    dag_name_input = driver.find_element(*dag_name_ipt)
    dag_name_input.send_keys(dag_name)
    driver.implicitly_wait(10)

    ack_dag_btn = driver.find_element(*ack_dag)
    ack_dag_btn.click()
    time.sleep(1)

    look_btn_1 = driver.find_element(*look_btn)
    look_btn_1.click()
    driver.implicitly_wait(10)

    for i in range(589, n):
        add_meta_data_btn = driver.find_element(*add_meta_data)
        add_meta_data_btn.click()

        time.sleep(1)

        meta_data_input = driver.find_element(*meta_data)
        meta_data_input.click()
        driver.implicitly_wait(10)

        None_category_input = driver.find_element(*None_category)
        None_category_input.click()
        driver.implicitly_wait(10)

        stock_btn = driver.find_element(*stock_item)
        stock_btn.click()
        time.sleep(0.5)

        factor_btn = driver.find_element(*stock_factor_1)
        factor_btn.click()
        time.sleep(0.5)

        # /html/body/div[3]/div/div/div/div/ul[4]/li[1]/div
        f_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/ul[4]/li[{}]'.format(i+1))
        f_btn.click()
        driver.implicitly_wait(10)
        job_type = driver.find_element(*jobType)
        job_type.click()
        driver.implicitly_wait(10)

        embed_formula_btn = driver.find_element(*embed_formula)
        embed_formula_btn.click()

        driver.implicitly_wait(10)
        ack_btn = driver.find_element(*add_meta_data_submit)
        ack_btn.click()

        time.sleep(1)


if __name__ == '__main__':
    sign_in()
    add_data_meta()
    # create_dag()