import page
from base.base_page import BasePage


# 新建联系人页面
class SettingPage(BasePage):

    # 点击添加按钮
    def click_my_btn(self):
        self.click_ele(page.my_btn)

    # 点击本地保存
    def click_local_save(self):
        self.click_ele(page.local_save)
