from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 首页 - 关闭
    close_button = By.ID, "com.yunmall.lc:id/img_close"

    # 首页 - 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    def click_close(self):
        self.click(self.close_button)

    def click_me(self):
        self.click(self.me_button)