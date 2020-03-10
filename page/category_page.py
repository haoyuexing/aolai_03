import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):

    goods_image_button = By.ID, "com.yunmall.lc:id/iv_img"

    def click_goods_image(self):
        goods_images = self.find_elements(self.goods_image_button)
        goods_images_count = len(goods_images)
        index = random.randint(0, goods_images_count-1)
        goods_images[index].click()

