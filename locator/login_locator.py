from selenium.webdriver.common.by import By

"""
    登录界面的UI元素定位
"""


login_address = (By.ID, 'login_address')
login_port = (By.ID, 'login_port')
login_username = (By.ID, 'login_username')
login_password = (By.ID, 'login_password')

login_submit = (By.XPATH, '/html/body/div/div/div/div[2]/form/div[3]/div/div/div/div/button')

