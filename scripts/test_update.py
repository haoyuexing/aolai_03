from base.base_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_update(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击我
        self.page.home.click_me()
        # 我 - 点击设置
        self.page.me.click_setting()
        # 设置 - 点击关于
        self.page.setting.click_about()
        # 关于 - 点击更新
        self.page.about.click_update()

        assert self.page.about.is_update_right_now_exist()
