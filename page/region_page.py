import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegionPage(BaseAction):

    area_feature = By.ID, "com.yunmall.lc:id/area_title"


    def click_region(self):
        """
        可以选择随机省市区
        :return:
        """

        while True:
            area_titles = self.find_elements(self.area_feature)
            area_titles_count = len(area_titles)
            index = random.randint(0, area_titles_count-1)
            area_titles[index].click()
            time.sleep(1)

            # 判断是否回到了编辑页面，如果是，则退出循环
            if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.AddressAddActivity":
                break




