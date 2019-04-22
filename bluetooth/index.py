#coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os

# desired_caps = {'platformName': 'Android',
#                 'deviceName': '9a762346',
#                 'platformVersion': '6.0.1',
#                 'noReset': True,
#                 'browserName':'Chrome'
#                 }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# print('浏览器启动成功')

import unittest
from time import sleep

class MyTestCase(unittest.TestCase):

    def setUp(self):
        capabilities = {
            "platformName": "Android",
            # Mobile OS类型
            "platformVersion": "4.4",
            # Mobile OS版本
            "deviceName": "3216e430",
            # adb devices
            "browserName": "Chrome",
            # Chrome浏览器
            "appPackage": "com.android.browser",
            # Chrome的包名
            "appActivity": ".BrowserActivity",
            # Chrome的启动页
            "unicodeKeyboard": True,
            # 支持中文输入，默认false
            "resetKeyboard": True,
            # 重置输入法为系统默认
            "noReset": True,
            # 不重新安装apk
            "noSign": True
            # 不重新签名apk
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        sleep(1)

    def test_chromeApp(self):
        url = "https://h5.m.taobao.com"
        # 手机淘宝H5
        driver = self.driver
        driver.get(url)
        sleep(1)
        driver.find_element_by_id("search-placeholder").click()
        # 点击淘宝搜索框
        sleep(1)
        driver.find_element_by_name("q").send_keys("华硕官方旗舰店")
        sleep(1)
        driver.find_element_by_class_name("icons-search").click()
        sleep(3)
        assert driver.page_source.__contains__("asus华硕官方旗舰店")

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
