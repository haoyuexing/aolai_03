from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    add_address_button = By.XPATH, "//*[@text='新增地址']"

    name_and_phone_label = By.ID, "com.yunmall.lc:id/receipt_name"

    def click_add_address(self):
        self.click(self.add_address_button)

    def get_first_name_and_phone_text(self):
        return self.get_text(self.name_and_phone_label)