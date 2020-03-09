from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 首页 - 关闭
    close_button = By.ID, "com.yunmall.lc:id/img_close"

    # 首页 - 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    def click_close(self):
        self.click(self.close_button)

    def click_me(self):
        self.click(self.me_button)

    def login_if_not(self, page):
        """
        如果没有登录就去登录，且最后会home的页面
        :param page:
        :return:
        """

        # 点击我
        self.click_me()

        # 判断登录状态
        # 获取当前页面的名字，根据名字是否为注册进行判断
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            # 回到首页
            page.me.click_home()
            return

        # 登录的代码
        # 注册 - 点击去登陆
        page.reg.click_login()
        # 登录 - 输入用户名
        page.login.input_username("itfeat")
        # 登录 - 输入密码
        page.login.input_password("123000")
        # 登录 - 点击登录
        page.login.click_login()


        # 回到首页
        page.me.click_home()