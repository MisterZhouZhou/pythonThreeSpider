from appium import webdriver
import time

cap = {
    "platformName": "Android",
    # Mobile OS类型
    "platformVersion": "8.1.0",
    # Mobile OS版本
    "deviceName": "emulator-5554",
    # adb devices
    'appPackage': 'com.example.beautifuldemo',
    'appActivity': 'com.example.beautifuldemo.MainActivity'
}

# cap = {
#     "platformName": "iOS",
#     # Mobile OS类型
#     "platformVersion": "11.4",
#     # Mobile OS版本
#     "deviceName": "iPhone 7",
#     # adb devices
#     "browserName": "safari",
# }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(3)
driver.quit()
