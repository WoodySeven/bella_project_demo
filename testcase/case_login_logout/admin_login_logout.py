#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import ddt
import logging
from lib.utils import capture_screen

test_data = [['admin', '123456', '退出'],
             ['invalid', '123456', '用户名不存在'],
             ['', '123456', '不可为空白']]

@ddt.ddt
class Bugfree管理员登录退出(unittest.TestCase):
    """
    演示的是bugfree的登录和退出
    数据驱动，相同的逻辑使用不同的数据去运行。
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*test_data)
    def test_admin_login_test(self, admin, password, flag):
        """admin的登录的所有测试用例"""
        logging.info("test_admin_login_test start....")
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys(admin)
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)
        logging.info("test data is : {}, {}, {}".format(admin, password, flag))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_admin_login_test end....")


if __name__ == '__main__':
    unittest.main()