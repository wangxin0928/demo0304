# 添加联系人页面
import page
from base.base_page import BasePage


class AddPage(BasePage):
    # 输入姓名
    def input_name(self, name):
        self.inout_ele(page.name, name)

    def input_phone(self, phone):
        self.inout_ele(page.phone, phone)
