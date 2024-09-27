from appnium.mini_Selenium_Program.Public.common.AppiumStart.AppiumStart import AppiumStart


def Release_conf():
    appnium = AppiumStart.Appnium
    appnium.quit()

    
def Quit_conf():
    appnium = AppiumStart.Appnium
    appnium.close()




