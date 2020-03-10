import time

from appium import webdriver


# 创建一个字典，包装相应的启动参数
from selenium.webdriver.common.by import By

desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = 'huawei p30'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.settings'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'


# 使用 uiautomator2 的框架
desired_caps['automationName'] = 'Uiautomator2'

# 连接appium服务器
driver = webdriver.Remote('http://192.168.1.106:4723/wd/hub', desired_caps)







def scroll_page_one_time(direction='up'):
    """
    在当前页面滑动一次
    :param direction:
        up: 从下往上
        down: 从上往下
        left: 从右往左
        right: 从左往右
    :return:
    """
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]

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
        driver.swipe(bottom_x, bottom_y, top_x, top_y)
    elif direction == "down":
        driver.swipe(top_x, top_y, bottom_x, bottom_y)
    elif direction == "left":
        driver.swipe(right_x, right_y, left_x, left_y)
    elif direction == "right":
        driver.swipe(left_x, left_y, right_x, right_y)
    else:
        raise Exception("这个方法只支持 up/down/left/right 请检查参数")

    time.sleep(1)



def find_element_with_scroll(feature, direction="up"):
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
            return driver.find_element(*feature)
        except Exception as e:
            # 滑动之前记录之前的pagesource
            page_source = driver.page_source
            scroll_page_one_time(direction)
            if driver.page_source == page_source:
                raise Exception("已经滑动到底，没有找到相关元素，请检查参数")

            time.sleep(2)





feature = By.XPATH, "//*[@text='关于平板电脑1']"
find_element_with_scroll(feature).click()
