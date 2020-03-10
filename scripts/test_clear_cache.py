from base.base_driver import init_driver
from page.page import Page


class TestClearCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_clear_cache(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击我
        self.page.home.click_me()
        # 我 - 点击设置
        self.page.me.click_setting()
        # 设置 - 点击清理缓存
        self.page.setting.click_clear_cache()

        assert self.page.setting.is_toast_exist("清理成功")