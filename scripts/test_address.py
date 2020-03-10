import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("address_data", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        detail = args["detail"]
        post_code = args["post_code"]
        toast = args["toast"]

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
        self.page.edit_address.input_name(name)
        # 编辑地址 - 输入手机号
        self.page.edit_address.input_phone(phone)
        # 编辑地址 - 输入详细地址
        self.page.edit_address.input_detail(detail)
        # 编辑地址 - 输入邮编
        self.page.edit_address.input_post_code(post_code)
        # 编辑地址 - 点击默认地址
        self.page.edit_address.click_default()
        # 编辑地址 - 点击选择区域
        self.page.edit_address.click_region()
        # 选择区域 - 开始选择
        self.page.region.click_region()

        # 编辑地址 - 保存
        self.page.edit_address.click_save()

        if toast is None:
            assert self.page.address_list.get_first_name_and_phone_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)

    def test_edit_address(self):

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
        # 地址列表 - 点击默认标记
        self.page.address_list.click_default()

        # 编辑地址 - 输入收件人
        self.page.edit_address.input_name("xiaoqiang")
        # 编辑地址 - 输入手机号
        self.page.edit_address.input_phone("17777777777")
        # 编辑地址 - 输入详细地址
        self.page.edit_address.input_detail("三单元 504")
        # 编辑地址 - 输入邮编
        self.page.edit_address.input_post_code("200000")

        # 编辑地址 - 点击选择区域
        self.page.edit_address.click_region()
        # 选择区域 - 开始选择
        self.page.region.click_region()

        # 编辑地址 - 保存
        self.page.edit_address.click_save()

        # 断言 是否有 保存成功的toast
        assert self.page.address_list.is_toast_exist("保存成功")
        # 断言 列表的第一个值 是否和刚刚输入的一样
        assert self.page.address_list.get_first_name_and_phone_text() == "%s  %s" % ("xiaoqiang", "17777777777")