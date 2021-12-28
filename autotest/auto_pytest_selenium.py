from selenium import webdriver
import time
import pytest


def login_Test(username,passwd):
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get("http://localhost:8848/wemall/user/login.htm")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="theForm"]/li[4]/input').click()


login_Test('lisi','852456')