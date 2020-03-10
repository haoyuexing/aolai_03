from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    detail_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    default_button = By.ID, "com.yunmall.lc:id/address_default"

    region_button = By.ID, "com.yunmall.lc:id/address_province"

    save_button = By.XPATH, "//*[@text='保存']"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self,text):
        self.input(self.phone_edit_text, text)

    def input_detail(self,text):
        self.input(self.detail_edit_text, text)

    def input_post_code(self,text):
        self.input(self.post_code_edit_text, text)

    def click_default(self):
        self.click(self.default_button)

    def click_region(self):
        self.click(self.region_button)

    def click_save(self):
        self.click(self.save_button)
