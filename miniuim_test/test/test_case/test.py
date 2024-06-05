import time
import minium


class Component(minium.MiniTest):
    def setUp(self) -> None:
        pass
        # minim = minium.Minium({
        #     # 替换成你的【小程序项目目录地址】
        #     "project_path": "C:/Users/10260/Desktop/小程序源代码/dist/dist/build/mp-weixin",
        #     # 替换成你的【开发者工具cli地址】
        #     "dev_tool_path": "D:/Program Files (x86)/Tencent/微信web开发者工具/cli.bat",
        # })
        # print(minim.get_system_info())

    def test_ui_op(self):
        print("开始执行测试脚本")

        # <----------------等待功能-------------------->
        #  等待页面跳转成功
        # ret = self.app.wait_for_page()
        # self.assertTrue(ret, "wait success")
        # #  等待页面异步加载完成
        # ret = self.app.wait_util(0.5)
        # self.assertTrue(ret, "wait success")
        # #  等待直到特定条件出现后，可能是页面元素，也可能是
        # ret = self.page.wait_for("view", max_timeout=20)
        # self.assertTrue(ret, "wait success")
        # #  等待页面的数据里特定的keys出现
        # keys = ("wait", "keys")
        # self.page.wait_data_contains(*keys, max_timeout=10)
        # self.assertTrue(ret, "wait success")
        # # <-----------------页面跳转---------------------->
        # #  跳tabBer需要使用switch_tab,在跳转时关闭所有非tabBer页面
        # self.app.switch_tab("/page/home")
        # # navigate_to只能用于页面跳转，不能跳转tabBer
        # self.app.navigate_to(url="/page/home")

        self.page.get_element("view", inner_text="请输入充电站名或地址").click()
        ret = self.page.wait_for("view.refresh-group", max_timeout=60)
        self.assertTrue(ret, "wait success")

        self.page.get_element("input").send_message("test")
        # # self.page.get_element(".navigator-text", inner_text="swiper").click()
        # # self.page.get_elements("switch")[0].click()
        # # self.page.get_elements("switch")[1].click()
        # print("test_ui_op执行测试完成")

    def tearDown(self) -> None:
        pass

