# 测试用例
import time

import pytest

from read_datas.read_data import build_address_func
from page.add_page import AddPage
from page.setting_page import SettingPage
from utils import get_driver


class TestAdd(object):
    # 通讯录测试类
    @pytest.fixture(autouse=True)
    def brfore_func(self):
        self.driver = get_driver()
        self.add_page = AddPage(self.driver)
        self.setting_page = SettingPage(self.driver)
        yield
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize('name,phone', build_address_func())
    def test_func(self, name, phone):
        # 点击添加按钮
        self.setting_page.click_my_btn()
        # 点击本地保存按钮
        self.setting_page.click_local_save()
        # 输入姓名
        self.add_page.input_name(name)
        # 输入电话
        self.add_page.input_phone(phone)
        # 发送返回键
        self.driver.keyevent(4)


        # # 点击添加按钮
        # self.setting_page.click_my_btn()
        # # 点击本地保存按钮
        # self.setting_page.click_local_save()
        # # 输入姓名
        # self.add_page.input_name('李白')
        # # 输入电话
        # self.add_page.input_phone('123456')
        # # 发送返回键
        # self.driver.keyevent(4)
    def test_func02(self):
        self.add_page.input_name('李白')
