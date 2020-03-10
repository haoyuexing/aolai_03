from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    add_address_button = By.XPATH, "//*[@text='新增地址']"

    def click_add_address(self):
        self.click(self.add_address_button)