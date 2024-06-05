import subprocess


def ConnectSimulator():
    try:
        cmd = "adb devices"
        n = "adb connect 127.0.0.1:7555"
        output = subprocess.check_output(cmd, shell=True)
        # 将命令输出转换为字符
        output_str = str(output)
        lines = output_str.strip().split(" ")

        for line in lines:
            if r"127.0.0.1:7555\tdevice" not in line:
                subprocess.check_output(n, shell=True)
    except ConnectionRefusedError:
        ConnectSimulator()


def cmdProcess(processName):
    try:
        # 使用tasklist命令获取系统进程信息
        cmd = 'tasklist'
        output = subprocess.check_output(cmd, shell=True)
        # 将命令输出转换为字符
        output_str = str(output)
        lines = output_str.strip().split(" ")
        # 分割字符串获取每一行
        # print(output_str)
        # 查找指定进程名称的状态
        for line in lines:
            if processName in line:
                return "服务已经启动"
    except ConnectionRefusedError:
        print(ConnectionRefusedError)


def AppiumApp_start():
    try:
        name = r'K\r\nAppium.exe'
        text = cmdProcess(name)
        processName = 'Appium.exe'
        if text != "服务已经启动":
            print(">>>>>>正在启动Appium服务器<<<<<<")
            app_name = r'C:\Users\10260\AppData\Local\Programs\Appium\Appium.exe'  # 或者 'C:\\Windows\\notepad.
            # 使用subprocess.run启动应用程序
            # subprocess.run(app_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            subprocess.Popen(app_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(">>>>>>启动Appium服务器完成<<<<<<")
        else:
            return text
    except ConnectionRefusedError:
        AppiumApp_start()


def Simulator_Start():
    try:
        name = r'K\r\nMuMuPlayer.exe'
        text = cmdProcess(name)
        if text != "服务已经启动":
            print(">>>>>>正在启动MuMu模拟器<<<<<<")
            app_name = r"D:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe"  # 或者 'C:\\Windows\\notepad.exe'
            # 使用subprocess.run启动应用程序
            subprocess.Popen(app_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(">>>>>>启动MuMu模拟器完成<<<<<<")
        else:
            return text
    except ConnectionRefusedError:
        Simulator_Start()


class getSimulatorState(object):
    def __init__(self, *loc):
        text = cmdProcess(loc)
        if text != "服务已经启动":
            print("--------------------小程序所需服务未启动,无法驱动小程序！----------------------")