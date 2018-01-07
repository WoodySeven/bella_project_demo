#!/usr/bin/env python
import unittest
import time
from selenium import webdriver


class BugfreeAdminLoginLogout(unittest.TestCase):
    """
    演示的是bugfree的登录和退出
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver

    def tearDown(self):
        pass

    def test_admin_login(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()