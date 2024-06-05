from appnium.mini_Selenium_Program.Public.Utils.uilts import Init
from appnium.mini_Selenium_Program.Public.Utils.SqlConnect import Connect


def Release_conf():
    appnium = Init().Appnium
    appnium.quit()

    
def Quiit_conf():
    appnium = Init().Appnium
    appnium.close()


def sql_release_conf():
    Connect.Cursor.close()


