import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsListPage(BaseAction):

    goods_detail_image_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    def click_goods_detail_image(self):
        goods_detail_images = self.find_elements(self.goods_detail_image_button)
        goods_detail_images_count = len(goods_detail_images)
        index = random.randint(0, goods_detail_images_count-1)
        goods_detail_images[index].click()


