from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 登录 - 用户名
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 登录 - 密码
    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 登录 - 登录按钮
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    def input_username(self, text):
        self.input(self.username_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_login(self):
        self.click(self.login_button)
