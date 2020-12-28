#! /usr/bin/python
# -*- coding: utf-8 -*-
from page.page_address import BaseAddress
from page.page_base import BasePage
from my_utils.get_data import get_data_from_ini
from my_configs import config


class MainPage(BasePage):

    def goto_address(self):
        """
        点击通讯录
        :return:
        """
        try:
            config.case_log.info('首页》点击通讯录')
            ele = get_data_from_ini(node='main',key='goto_address')
            self._wait_element_to_click(method=ele[0],message=ele[1])
            self._find_element_and_click(method=ele[0],message=ele[1])
            config.case_log.info('首页》点击通讯录：success')
            return BaseAddress(self._driver)
        except Exception as e:
            config.case_log.error('首页》点击通讯录：error')
            raise e
