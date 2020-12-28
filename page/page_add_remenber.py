#! /usr/bin/python
# -*- coding: utf-8 -*-

from page.page_base import BasePage
from  my_utils.get_data import get_data_from_ini
from my_configs import config

class AddRemenber(BasePage):

    def add_remenber_success(self,name,sex,phone):
        """
        添加成员页面》手动添加成员
        :return:
        """
        # 点击手动添加成员
        try:
            config.case_log.info('点击手动添加成员')
            ele = get_data_from_ini(node='add_remenber',key='add_remenber')
            self._wait_element_to_click(method=ele[0],message=ele[1])
            self._find_element_and_click(method=ele[0],message=ele[1])
            config.case_log.info('点击手动添加成员：success')
        except Exception as e:
            config.case_log.error('点击手动添加成员：error')
            raise e
        # 输入姓名
        try:
            config.case_log.info('输入姓名')
            ele = get_data_from_ini(node='add_remenber',key='add_remenber_name')
            self._wait_element_to_click(method=ele[0],message=ele[1])
            self._find_element_and_sendkeys(method=ele[0],message=ele[1],text=name)
            config.case_log.info('输入姓名：success')
        except Exception as e:
            config.case_log.error('输入姓名：error')
            raise e
        # 选择性别
        try:
            config.case_log.info('选择性别')
            ele = get_data_from_ini(node='add_remenber', key='add_remenber_sex')
            self._find_element_and_click(method=ele[0],message=ele[1])
            method = 'xpath'
            message = f'//*[@class="android.widget.ListView"]//*[@text="{sex}"]'
            self._wait_element_to_click(method=method,message=message)
            self._find_element_and_click(method=method,message=message)
            config.case_log.info('选择性别：success')
        except Exception as e:
            config.case_log.error('选择性别：error')
            raise e
        # 输入手机号
        try:
            config.case_log.info('输入手机号')
            ele = get_data_from_ini(node='add_remenber', key='add_remenber_phone')
            self._wait_element_to_click(method=ele[0],message=ele[1])
            self._find_element_and_sendkeys(method=ele[0],message=ele[1],text=phone)
            config.case_log.info('输入手机号：success')
        except Exception as e:
            config.case_log.error('输入手机号：error')
            raise e
        # 点击保存
        try:
            config.case_log.info('点击保存')
            ele = get_data_from_ini(node='add_remenber', key='add_remenber_save')
            self._find_element_and_click(method=ele[0],message=ele[1])
            config.case_log.info('点击保存：success')
        except Exception as e:
            config.case_log.error('点击保存：error')
            raise e

        return AddRemenber(self._driver)





    def get_addremenber_toast(self):
        text = self._get_toast().text
        return text

    def back_to_address(self):
        """
        添加成员页面返回通讯录页面
        :return:
        """
        try:
            from page.page_address import BaseAddress
            config.case_log.info('添加成员页面返回通讯录页面')
            ele = get_data_from_ini(node='add_remenber', key='add_remenber')
            self._wait_element_to_click(method=ele[0], message=ele[1])
            ele = get_data_from_ini(node='add_remenber', key='add_remenber_back_to_address')
            self._find_element_and_click(method=ele[0], message=ele[1])
            config.case_log.info('添加成员页面返回通讯录页面：success')
            return BaseAddress(self._driver)
        except Exception as e:
            config.case_log.error('添加成员页面返回通讯录页面：error')
            raise e






