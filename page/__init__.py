from selenium.webdriver.common.by import By

# 通讯录列表页面
# 新建联系人按钮
my_btn = (By.ID, 'com.android.contacts:id/floating_action_button')
# 本地保存
local_save = (By.XPATH, '//*[@text="本地保存"]')

# 姓名
name = (By.XPATH, '//*[@text="姓名"]')
# 电话
phone = (By.XPATH, '//*[@text= "电话"]')
