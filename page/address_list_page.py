import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    add_address_button = By.XPATH, "//*[@text='新增地址']"

    name_and_phone_label = By.ID, "com.yunmall.lc:id/receipt_name"

    default_label = By.ID, "com.yunmall.lc:id/address_is_default"

    edit_button = By.XPATH, "//*[@text='编辑']"

    delete_button = By.XPATH, "//*[@text='删除']"

    commit_button = By.XPATH, "//*[@text='确认']"

    def click_add_address(self):
        self.click(self.add_address_button)

    def get_first_name_and_phone_text(self):
        return self.get_text(self.name_and_phone_label)

    def click_default(self):
        self.click(self.default_label)

    def click_edit(self):
        self.click(self.edit_button)

    def click_delete(self):
        self.click(self.delete_button)

    def click_commit(self):
        self.click(self.commit_button)

    def is_default_label_exist(self):
        return self.is_element_exist(self.default_label)

    def delete_address_ten_time(self):
        """
        循环删除十次地址，如果有的话
        :return:
        """
        for i in range(10):
            self.click_edit()
            try:
                self.click_delete()
            except TimeoutException as e:
                return
            self.click_commit()