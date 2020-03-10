import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):

    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    commit_button = By.XPATH, "//*[@text='确认']"

    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    def click_commit(self):
        self.click(self.commit_button)

    def choose_spec(self):
        """
        选择规格
        :return:
        """
        while True:
            self.click_commit()

            if self.is_toast_exist("成功加入"):
                break
            self.click_commit()
            toast_text = self.get_toast_text("请选择")

            # try:
            #     toast_text = self.get_toast_text("请选择")
            # except TimeoutException as e:
            #     break

            should_choose_spec = toast_text.split(" ")[1]
            xpath = "//*[@text='%s']/../*[2]/*[1]" % should_choose_spec
            self.click((By.XPATH, xpath))
        


