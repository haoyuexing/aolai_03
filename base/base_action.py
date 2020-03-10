import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=10.0, poll=1.0):
        self.clear(feature, timeout, poll)
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).clear()

    def get_text(self, feature, timeout=10.0, poll=1.0):
        return self.find_element(feature, timeout, poll).text

    def is_toast_exist(self, text):
        try:
            self.find_element((By.XPATH, "//*[contains(@text, '" + text + "')]"), 5, 0.1)
            return True
        except Exception as e:
            return False

    def scroll_page_one_time(self, direction='up'):
        """
        在当前页面滑动一次
        :param direction:
            up: 从下往上
            down: 从上往下
            left: 从右往左
            right: 从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        bottom_x = center_x
        bottom_y = screen_height * 0.75
        top_x = center_x
        top_y = screen_height * 0.25
        right_x = screen_width * 0.75
        right_y = center_y
        left_x = screen_width * 0.25
        left_y = center_y

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        else:
            raise Exception("这个方法只支持 up/down/left/right 请检查参数")

        time.sleep(1)

    def find_element_with_scroll(self, feature, direction="up"):
        """
        根据元素的特征和方法边滑边找
        :param feature: 元素的特征
        :param direction: 方向
            up: 从下往上
            down: 从上往下
            left: 从右往左
            right: 从左往右
        :return: 元素本身
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception as e:
                # 滑动之前记录之前的page_source
                page_source = self.driver.page_source
                self.scroll_page_one_time(direction)
                if self.driver.page_source == page_source:
                    raise Exception("已经滑动到底，没有找到相关元素，请检查参数")

                time.sleep(2)


