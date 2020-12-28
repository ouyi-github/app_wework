#! /usr/bin/python
# -*- coding: utf-8
import time

from page.page_add_remenber import AddRemenber
from page.page_base import BasePage
from my_utils.get_data import get_data_from_ini
from my_configs import config

class BaseAddress(BasePage):

    def goto_add_remenber(self):
        """
        通讯录页面》添加用户
        :return:
        """
        try:
            config.case_log.info('通讯录页面》添加用户')
            ele = get_data_from_ini(node='address',key='add_remenber')
            self._swip_find_element_and_click(method=ele[0],message=ele[1])
            config.case_log.info('通讯录页面》添加用户：success')
            return AddRemenber(self._driver)
        except Exception as e:
            config.case_log.error('通讯录页面》添加用户：error')
            raise e

    def get_remenber_by_name(self,name):
        """
        获取通讯录指定成员的姓名
        :return:
        """
        try:
            config.case_log.info(f'获取通讯录指定成员{name}的姓名')
            time.sleep(1)
            message = f'//*[@class="android.widget.ListView"]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout//android.widget.TextView[@text="{name}"]'
            ele = get_data_from_ini(node='address', key='add_remenber')
            # while True:
            #     eles  = self._find_elments(method='xpath',message=message)
            #     ele_finish = self._swip_find_element(method=ele[0],message=ele[1])
            #     if ele_finish:
            #         break
            eles = self._find_elments(method='xpath', message=message)
            res_list = [i.text for i in eles]
            config.case_log.info(f'获取通讯录指定成员{name}的姓名：success')
            return res_list
        except Exception as e:
            config.case_log.error(f'获取通讯录指定成员{name}的姓名：error')
            raise e





