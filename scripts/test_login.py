import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)


    def teardown(self):
        self.driver.quit()

    def test_hello(self):
        # 首页 - 点击关闭
        self.page.home.click_close()

        # 判断 登录状态
        self.page.home.login_if_not(self.page)



    # @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     toast = args["toast"]
    #
    #     # 首页 - 点击关闭
    #     self.page.home.click_close()
    #     # 首页 - 点击我
    #     self.page.home.click_me()
    #     # 注册 - 点击去登陆
    #     self.page.reg.click_login()
    #     # 登录 - 输入用户名
    #     self.page.login.input_username(username)
    #     # 登录 - 输入密码
    #     self.page.login.input_password(password)
    #     # 登录 - 点击登录
    #     self.page.login.click_login()
    #
    #     # 判断用那种方式断言
    #     if toast is None:
    #         # 我 - 进行断言
    #         assert self.page.me.get_nikename_text() == username
    #     else:
    #         # 使用 toast 断言
    #         assert self.page.login.is_toast_exist(toast)

