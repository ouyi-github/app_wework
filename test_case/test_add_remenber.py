import logging
import os

import allure
import pytest

from page.page_base import BasePage
from page.page_main import MainPage
from my_configs import config
from my_utils.get_data import get_data_from_yaml

@allure.story('添加成员')
class TestRemenber:
    data_success = get_data_from_yaml(os.path.join(config.BASE_DIR,'data/case_data/add_remenber.yaml'))['success']
    def setup(self):
        self.mainpage = MainPage()

    @allure.title('添加成员成功case')
    @pytest.mark.parametrize('name,sex,phone',data_success)
    def test_addremenber_success(self,name,sex,phone):
        with allure.step('首页》点击通讯录'):
            res = self.mainpage.goto_address()
        with allure.step('通讯录页面》点击添加成员'):
            res = res.goto_add_remenber()
        with allure.step('添加成员页面》添加成员'):
            res = res.add_remenber_success(name=name,sex=sex,phone=phone)
        with allure.step('添加成员页面》返回通讯录'):
            res = res.back_to_address()
        assert name in res.get_remenber_by_name(name)




if __name__ == "__main__":
    result = config.result_path
    report = config.report_path
    pytest.main(['-vs', 'test_add_remenber.py', f'--alluredir={result}'])
    os.system(f'allure generate {result} -o {report}')

