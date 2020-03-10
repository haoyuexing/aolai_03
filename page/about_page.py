from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    update_button = By.XPATH, "//*[@text='版本更新']"

    update_right_now_button = By.ID, "com.yunmall.lc:id/btn_update"

    def click_update(self):
        self.click(self.update_button)

    def is_update_right_now_exist(self):
        return self.is_element_exist(self.update_right_now_button)