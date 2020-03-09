from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 点击我
        self.page.home.click_me()
        # 注册 - 点击去登陆
        self.page.reg.click_login()
        # 登录 - 输入用户名
        self.page.login.input_username("17611675774")
        # 登录 - 输入密码
        self.page.login.input_password("123000")
        # 登录 - 点击登录
        self.page.login.click_login()
        # 我 - 进行断言
        assert self.page.me.get_nikename_text() == "itfeat"
