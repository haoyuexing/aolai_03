from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_shop_cart(self):
        # 首页 - 点击关闭
        self.page.home.click_close()
        # 首页 - 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 首页 - 点分类
        self.page.home.click_category()
        # 分类 - 随机点一张图
        self.page.category.click_goods_image()
        # 商品列表 - 随机点一张图
        self.page.goods_list.click_goods_detail_image()
        # 商品详情 - 加入购物车
        self.page.goods_detail.click_add_shop_cart()


