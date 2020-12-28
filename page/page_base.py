#! /usr/bin/python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from my_configs import config


class BasePage:
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            caps = {}
            caps['platformName'] = 'Android'  # 被测设备为Android
            caps['platformVersion'] = '5.1.1'  # 被测设备系统版本
            caps['deviceName'] = '127.0.0.1:21503'  # 被测设备
            caps['appActivity'] = '.launch.WwMainActivity'  # 被测app要打开的页面
            caps['appPackage'] = 'com.tencent.wework'  # 被测app的包名
            caps['noReset'] = 'true'  # 启动时是否不重置app，可以跳过登录等
            caps['unicodeKeyboard'] = 'true'  # 设置中文输入
            caps['resetKeyboard'] = 'true'  # 设置中文输入
            caps['settings[waitForIdleTimeout]'] = 0
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

    def _find_element(self,method,message):
        """
        二次封装查找元素方法
        :param method: example:id
        :param message: example: 'kw'
        """
        try:
            if method == "id":
                ele = self._driver.find_element(MobileBy.ID, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == "name":
                ele = self._driver.find_element(MobileBy.NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == "xpath":
                ele = self._driver.find_element(MobileBy.XPATH, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == "css":
                ele = self._driver.find_element(MobileBy.CSS_SELECTOR, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'class':
                ele = self._driver.find_element(MobileBy.CLASS_NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'link_text':
                ele = self._driver.find_element(MobileBy.LINK_TEXT, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'partial_link_text':
                ele = self._driver.find_element(MobileBy.PARTIAL_LINK_TEXT, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'tag_name':
                ele = self._driver.find_element(MobileBy.TAG_NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'android_uiautomator':
                ele = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
            elif method == 'accessibility':
                ele = self._driver.find_element(MobileBy.ACCESSIBILITY_ID,message)
                config.case_log.info(f'find element success (method={method},message={message})')
                return ele
        except Exception as e:
            config.case_log.error(f'find element failed (method={method},message={message})')
            raise e


    def _find_elments(self,method,message):
        """
        二次封装查找多元素方法
        :param method: example:id
        :param message: example: 'kw'
        """
        try:
            if method == "id":
                ele = self._driver.find_elements(MobileBy.ID, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == "name":
                ele = self._driver.find_elements(MobileBy.NAME, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == "xpath":
                ele = self._driver.find_elements(MobileBy.XPATH, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == "css":
                ele = self._driver.find_elements(MobileBy.CSS_SELECTOR, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'class':
                ele = self._driver.find_elements(MobileBy.CLASS_NAME, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'link_text':
                ele = self._driver.find_elements(MobileBy.LINK_TEXT, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'partial_link_text':
                ele = self._driver.find_elements(MobileBy.PARTIAL_LINK_TEXT, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'tag_name':
                ele = self._driver.find_elements(MobileBy.TAG_NAME, message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'android_uiautomator':
                ele = self._driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
            elif method == 'accessibility':
                ele = self._driver.find_elements(MobileBy.ACCESSIBILITY_ID,message)
                config.case_log.info(f'find elements success (method={method},message={message})')
                return ele
        except Exception as e:
            config.case_log.error(f'find elements failed (method={method},message={message})')
            raise e

    def _find_element_and_click(self,method,message):
        """
        封装查找元素并点击的方法
        :return:
        """
        try:
            if method == "id":
                ele = self._driver.find_element(MobileBy.ID, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == "name":
                ele = self._driver.find_element(MobileBy.NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == "xpath":
                ele = self._driver.find_element(MobileBy.XPATH, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == "css":
                ele = self._driver.find_element(MobileBy.CSS_SELECTOR, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'class':
                ele = self._driver.find_element(MobileBy.CLASS_NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'link_text':
                ele = self._driver.find_element(MobileBy.LINK_TEXT, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'partial_link_text':
                ele = self._driver.find_element(MobileBy.PARTIAL_LINK_TEXT, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'tag_name':
                ele = self._driver.find_element(MobileBy.TAG_NAME, message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'android_uiautomator':
                ele = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
            elif method == 'accessibility':
                ele = self._driver.find_element(MobileBy.ACCESSIBILITY_ID,message)
                config.case_log.info(f'find element success (method={method},message={message})')
                ele.click()
                config.case_log.info(f'click element success (method={method},message={message})')
                return
        except Exception as e:
            config.case_log.error(f'click element failed (method={method},message={message})')
            raise e


    def _find_element_and_sendkeys(self,method,message,text):
        try:
            ele = self._find_element(method,message)
            ele.send_keys(text)
            config.case_log.info(f'sendkeys {text} to element success (method={method},message={message})')
        except Exception as e:
            config.case_log.error(f'sendkeys {text} to element error (method={method},message={message})')

    def _wait_element_to_click(self,method,message):
        try:
            if method == "id":
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ID,message)))
            elif method == "name":
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.NAME,message)))
            elif method == "xpath":
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,message)))
            elif method == "css":
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.CSS_SELECTOR,message)))
            elif method == 'class':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.CLASS_NAME,message)))
            elif method == 'link_text':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.LINK_TEXT,message)))
            elif method == 'partial_link_text':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.PARTIAL_LINK_TEXT,message)))
            elif method == 'tag_name':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.TAG_NAME,message)))
            elif method == 'android_uiautomator':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,message)))
            elif method == 'accessibility':
                WebDriverWait(self._driver,timeout=10).until(expected_conditions.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,message)))
        except Exception as e:
            config.case_log.error(f'wait element to clickable error (method={method},message={message})')
            raise e

    def _swip_find_element(self,method,message):
        """
        自定义滑动查找元素
        :param method:
        :param message:
        :return:
        """
        while True:
            w_size = self._driver.get_window_size()
            w_x = w_size['width']
            w_y = w_size['height']
            x = int(w_x) / 2
            y1 = int(w_y) * 0.8
            y2 = int(w_y) * 0.2
            action = TouchAction(self._driver)
            action.press(x=int(x),y=int(y1))
            action.move_to(x=int(x),y=int(y2))
            action.release()
            action.perform()
            element = self._find_element(method=method,message=message)
            if element:
                break
        return element


    def _swip_find_element_and_click(self,method,message):
        """
        自定义滑动查找元素并点击
        :param method:
        :param message:
        :return:
        """
        while True:
            ss = False
            try:
                element = self._find_element(method=method, message=message)
                element.click()
                ss = True
                config.case_log.info(f'click element success (method={method},message={message})')
            except:
                pass
            if ss:
                break
            w_size = self._driver.get_window_size()
            w_x = w_size['width']
            w_y = w_size['height']
            x = int(w_x) / 2
            y1 = int(w_y) * 0.8
            y2 = int(w_y) * 0.2
            action = TouchAction(self._driver)
            action.press(x=int(x),y=int(y1))
            action.move_to(x=int(x),y=int(y2))
            action.release()
            action.perform()
        return

    def _get_toast(self):
        """
        获取页面Toast
        :return:
        """
        try:
            ele = self._driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
            config.case_log.info('获取页面Toast：success')
            return ele
        except Exception as e:
            config.case_log.error('获取页面Toast：error')
            raise e









if __name__ == "__main__":
    BasePage()._swip_find_element()





