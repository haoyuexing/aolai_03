import time

from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import init_driver
from page.page import Page


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

        print(self.driver.page_source)

    def teardown(self):
        self.driver.quit()

    def test_vip(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击我
        self.page.home.click_me()
        # 我 - 点击成为vip
        self.page.me.click_vip()

        # vip - 输入邀请码
        self.page.vip.input_code("hello")
        # vip - 点击立即成为会员
        self.page.vip.click_vip()

        assert self.page.vip.is_not_vip("邀请码输入不正确")





