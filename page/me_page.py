from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    nikename_label = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    def get_nikename_text(self):
        return self.get_text(self.nikename_label)

    def click_home(self):
        self.click(self.home_button)