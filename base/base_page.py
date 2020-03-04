from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, loction, timeout=5, poll=1):
        # 定位元素  --- 使用显示等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(loction[0], loction[1]))
        return element

    # 点击操作
    def click_ele(self, loction):
        self.find_ele(loction).click()

    # 输入操作
    def inout_ele(self, loction, text):
        ele = self.find_ele(loction)
        ele.clear()
        ele.send_keys(text)
