import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from 运营平台自动化.pom.public.logincode import Login2
from selenium.webdriver.common.keys import Keys
from 运营平台自动化.pom.public.public import Public
from 运营平台自动化.pom.test_case.Send_Pack import Send_Pack


class Pack_Create(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = ''
        Login2().test_login2(self.driver)
        self.PUBLIC = Public(self.driver, self.url)

    def test_StoredValue_Card_Create(self):
        # 强制等待资源中心出现并点击
        self.PUBLIC.Action_WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        # 访问卡包管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[5]'),
                                '无法访问卡包管理')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '无法访问卡包界面的element')
        # 点击创建储值卡按钮
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[2]/div/div[1]/div/span[1]/button'),
                                '找不到新建储值卡按钮')
        # 切换到创建储值卡界面
        self.PUBLIC.Switch_Window()
        # 进入创建储值卡界面的嵌入式界面
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到创建储值卡弹窗的element')
        # 输入储值卡名
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[2]/div[1]/input'), '9-2-21')
        # self.PUBLIC.Send_key((By.XPATH, '//*[@id="partnerId"]'), '不绑定集团')
        # 选择有效类型label[1]:1是长期有效，2是定期有效，3是累计有效，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[4]/div[1]/div/label[3]')
        if self.PUBLIC.Find_element_Class(By.XPATH,
                                          '//*[@id="cpPlane"]/div/form/div[4]/div[1]/div/label[3]') == 'el-radio is-checked':
            # 累计有效的冻结设置：label[1],1冻结,2是过期清零
            self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[5]/div[1]/label[2]')
        # 选择使用范围  label[1]:1是自营充电站，2是指定充电站，3是所有充电站，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[6]/div[1]/label[2]')
        if self.PUBLIC.Find_element_Class(By.XPATH, '//*[@id="cpPlane"]/div/form/div[6]/div[1]/label[2]') == 'el-radio is-checked':
            self.Input_Message()
        # 点击确认按钮
        time.sleep(2)
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/input[1]')
        # Assert().assertTest(self.driver)
        Send_Pack().test_Send_Card(self.driver)

    def test_Deduction_Card_Create(self):
        # 强制等待资源中心出现并点击
        self.PUBLIC.Action_WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        # 访问卡包管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[5]'),
                                '无法访问卡包管理')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '无法访问卡包界面的element')
        # 点击抵扣卡页签
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[1]/div/ul/li[2]'), '无法访问到抵扣卡页的element')
        # 点击创建抵扣卡按钮
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[2]/div/div[1]/div/span[2]/button'),
                                '找不到新建抵扣卡按钮')
        # 切换到创建抵扣卡界面
        self.PUBLIC.Switch_Window()
        # 进入创建抵扣卡界面的嵌入式界面
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到创建抵扣卡弹窗的element')
        # 输入抵扣卡名
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[2]/div[1]/input'), '9-22')
        # self.PUBLIC.Send_key((By.XPATH, '//*[@id="partnerId"]'), '不绑定集团')
        # 选择抵扣对象:label[1],1是服务费，2是电费，默认是服务费
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[3]/div/label[2]')
        # 优惠叠加：label[1],1是不叠加使用，2.是可叠加使用，默认是不可叠加使用
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[4]/div[1]/label[2]')
        # 选择有效类型label[1]:1是长期有效，2是定期有效，3是累计有效，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[5]/div[1]/div/label[3]')
        if self.PUBLIC.Find_element_Class(By.XPATH,
                                          '//*[@id="cpPlane"]/div/form/div[5]/div[1]/div/label[3]') == 'el-radio is-checked':
            # 累计有效的冻结设置：label[1],1冻结,2是过期清零
            self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[6]/div[1]/label[2]')
        # 选择使用范围  label[1]:1是自营充电站，2是指定充电站，3是所有充电站，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[1]/label[2]')
        if self.PUBLIC.Find_element_Class(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[1]/label[2]') == 'el-radio is-checked':
            self.Input_Message()
        # 点击确认按钮
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/input[1]')
        # Assert().assertTest(self.driver)
        Send_Pack().test_Send_Card(self.driver)

    def test_Energy_Card_Create(self):
        # 强制等待资源中心出现并点击
        self.PUBLIC.Action_WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        # 访问卡包管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[5]'),
                                '无法访问卡包管理')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '无法访问卡包界面的element')
        # 点击能量卡页签
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[1]/div/ul/li[3]'), '无法访问到能量卡页的element')
        # 点击创建能量卡按钮
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[2]/div/div[1]/div/span[3]/button'),
                                '找不到新建能量卡按钮')
        # 切换到创建能量卡界面
        self.PUBLIC.Switch_Window()
        # 进入创建能量卡界面的嵌入式界面
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到创建能量卡弹窗的element')
        # 输入能量卡名
        time.sleep(2)
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[2]/div[1]/input'), '9-22')
        # self.PUBLIC.Send_key((By.XPATH, '//*[@id="partnerId"]'), '不绑定集团')
        # 周期设置:label[1],1是日，2是周，3是月，默认是日
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[4]/div[1]/label[2]')
        # 额度类型：label[1],1是充电电量，2.是充电时长，默认是充电电量
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[5]/div/label[2]')
        self.driver.execute_script('window.scrollTo(0,530)')
        # 每日限制：label[1]:1是关闭，2是开启，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[1]/label[2]')
        time.sleep(2)
        if self.PUBLIC.Find_element_Class(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[1]/label[2]') == 'el-radio is-focus is-checked':
            # 填写每天可用得额度
            self.PUBLIC.ClearKey(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[2]/div/div/input')
            self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div[2]/div/div/input'), '10.00')
        # 使用时间控制：label[1]：1是全天， 2是每日可用时段
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[8]/div[1]/label[2]')
        time.sleep(1)
        if self.PUBLIC.Find_element_Class(By.XPATH, '//*[@id="cpPlane"]/div/form/div[8]/div[1]/label[2]') == 'el-radio is-focus is-checked':
            # 填写每天可用得额度
            self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="cpPlane"]/div/form/div[8]/div[2]/div/div[1]'), '无法选择开始时间')
            self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="cpPlane"]/div/form/div[8]/div[2]/div/div[12]'), '无法选择结束时间')
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,530)')
        self.PUBLIC.Click(By.XPATH, '/html/body/div[2]/div/div/form/div[9]/div/label[2]')
        if self.PUBLIC.Find_element_Class(By.XPATH, '/html/body/div[2]/div/div/form/div[9]/div/label[2]') == 'el-radio is-checked':
            self.Input_Message()
        # 点击确认按钮
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/input[1]')
        # Assert().assertTest(self.driver)
        Send_Pack().test_Send_Card(self.driver)

    def test_Energy_Deduction_Card_Create(self):
        # 强制等待资源中心出现并点击
        self.PUBLIC.Action_WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/a/span'), '无法点击资源中心')
        # 访问卡包管理界面
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="wrapper"]/div[2]/nav/ul[1]/li[2]/ul/li[2]/ul/li[5]'),
                                '无法访问卡包管理')
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="page-content"]/iframe[2]'), '无法访问卡包界面的element')
        # 点击能量抵扣卡页签
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[1]/div/ul/li[4]'), '无法访问到能量抵扣卡页的element')
        # 点击创建能量抵扣卡按钮
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="cpIndex"]/div/div[2]/div/div[1]/div/span[4]/button'),
                                '找不到新建能量抵扣卡按钮')
        # 切换到创建能量抵扣抵扣卡界面
        self.PUBLIC.Switch_Window()
        # 进入创建能量抵扣卡界面的嵌入式界面
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到创建能量抵扣卡弹窗的element')
        # 输入能量抵扣卡名
        time.sleep(2)
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[2]/div[1]/input'), '9-22')
        # 抵扣对象：label[1]:1是服务费，2是电费
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[3]/div/label[2]')
        # 优惠叠加:label[1],1是不叠加，2是可叠加
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[4]/div[1]/label[2]')
        # 周期设置:label[1],1是日，2是周，3是月，默认是日
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[6]/div[1]/label[2]')
        # 额度类型：label[1],1是充电电量，2.是充电时长，默认是充电电量
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[7]/div/label[2]')
        self.driver.execute_script('window.scrollTo(0,530)')
        # 每日限制：label[1]:1是关闭，2是开启，默认是长期有效
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[9]/div[1]/label[2]')
        time.sleep(2)
        if self.PUBLIC.Find_element_Class(By.XPATH,
                                          '//*[@id="cpPlane"]/div/form/div[9]/div[1]/label[2]') == 'el-radio is-focus is-checked':
            # 填写每天可用得额度
            self.PUBLIC.ClearKey(By.XPATH, '//*[@id="cpPlane"]/div/form/div[9]/div[2]/div/div/input')
            self.PUBLIC.Send_key((By.XPATH, '//*[@id="cpPlane"]/div/form/div[9]/div[2]/div/div/input'), '10.00')
        # 使用时间控制：label[1]：1是全天， 2是每日可用时段
        self.PUBLIC.Click(By.XPATH, '//*[@id="cpPlane"]/div/form/div[10]/div[1]/label[2]')
        time.sleep(1)
        if self.PUBLIC.Find_element_Class(By.XPATH,
                                          '//*[@id="cpPlane"]/div/form/div[10]/div[1]/label[2]') == 'el-radio is-focus is-checked':
            # 填写每天可用得额度
            self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="cpPlane"]/div/form/div[10]/div[2]/div/div[1]'),
                                            '无法选择开始时间')
            self.PUBLIC.Action_WaitElements((By.XPATH, '//*[@id="cpPlane"]/div/form/div[10]/div[2]/div/div[12]'),
                                            '无法选择结束时间')
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,600)')
        self.PUBLIC.Click(By.XPATH, '/html/body/div[2]/div/div/form/div[11]/div/label[2]')
        if self.PUBLIC.Find_element_Class(By.XPATH,
                                          '/html/body/div[2]/div/div/form/div[11]/div/label[2]') == 'el-radio is-checked':
            self.Input_Message()
        # 点击确认按钮
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/input[1]')
        # Assert().assertTest(self.driver)
        Send_Pack().test_Send_Card(self.driver)

    def Input_Message(self):
        self.PUBLIC.Switch_Window()
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe2"]'), '找不到该iframe的element')
        # 强制等待搜索按钮出现并点击
        self.PUBLIC.WaitElement((By.XPATH, '//*[@id="btn-search"]'), '找不到搜索按钮')
        time.sleep(5)
        # 填写站点名
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="name"]'), '2.0协议站')
        # 回车
        self.PUBLIC.Send_key((By.XPATH, '//*[@id="name"]'), Keys.ENTER)
        # 选择搜索的站点
        time.sleep(2)
        self.PUBLIC.Click(By.XPATH, '//*[@id="jqg_grid_0"]')
        # 点击确认选择添加的资源(站点)
        self.PUBLIC.Click(By.XPATH, '//*[@id="actions"]/button')
        # 切换回创建卡信息填写弹窗
        self.PUBLIC.Switch_Window()
        self.PUBLIC.Frame_switch_window((By.XPATH, '//*[@id="layui-layer-iframe1"]'), '找不到创建卡弹窗的element')

    def tearDown(self) -> None:
        self.driver.quit()
