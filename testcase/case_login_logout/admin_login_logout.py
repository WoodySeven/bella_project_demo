#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import ddt

test_data = [['admin', '123456', '退出'],
             ['invalid', '123456', '用户名不存在'],
             ['', '123456', '不可为空白'],
             ['sss', '123456', '用户名不存在']]
@ddt.ddt
class Bugfree管理员登录退出(unittest.TestCase):
    """
    演示的是bugfree的登录和退出
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.87"
        driver = self.driver


    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*test_data)
    def test_admin_login(self, admin, password, flag):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys(admin)
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn(flag,driver.page_source)


if __name__ == '__main__':
    unittest.main()