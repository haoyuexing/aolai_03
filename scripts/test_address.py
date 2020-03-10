import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_address(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点击我
        self.page.home.click_me()
        # 我 - 点击设置
        self.page.me.click_setting()
        # 设置 - 点击地址管理
        self.page.setting.click_address_list()
        # 地址列表 - 点击新增地址
        self.page.address_list.click_add_address()
        # 编辑地址 - 输入收件人
        self.page.edit_address.input_name("xiaoming")
        # 编辑地址 - 输入手机号
        self.page.edit_address.input_phone("18888888888")
        # 编辑地址 - 输入详细地址
        self.page.edit_address.input_detail("二单元 808")
        # 编辑地址 - 输入邮编
        self.page.edit_address.input_post_code("100000")
        # 编辑地址 - 点击默认地址
        self.page.edit_address.click_default()
        # 编辑地址 - 点击选择区域
        self.page.edit_address.click_region()
        # 选择区域 - 开始选择
        self.page.region.click_region()

        # 编辑地址 - 保存
        self.page.edit_address.click_save()

        assert self.page.address_list.get_first_name_and_phone_text() == "xiaoming  18888888888"

