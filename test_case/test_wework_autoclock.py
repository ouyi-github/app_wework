#! /usr/bin/python
# -*- coding: utf-8 -*-
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
class TestAutoClock:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android' # 被测设备为Android
        caps['platformVersion'] = '5.1.1' # 被测设备系统版本
        caps['deviceName'] = '127.0.0.1:21503' # 被测设备
        caps['appActivity'] = '.launch.WwMainActivity' # 被测app要打开的页面
        caps['appPackage'] = 'com.tencent.wework' # 被测app的包名
        caps['noReset'] = 'true' # 启动时是否不重置app，可以跳过登录等
        caps['unicodeKeyboard'] = 'true' # 设置中文输入
        caps['resetKeyboard'] = 'true' # 设置中文输入
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_autoclock(self):
        """
        企业微信自动打卡
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("").instance(0));').click()
        # 滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="外出打卡"]').click()

        # 查找text包含xx的元素
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()
        time.sleep(2)
        assert '外出打卡成功' in self.driver.page_source
        
if __name__ == "__main__":
    pytest.main(['-vs','test_wework_autoclock.py'])