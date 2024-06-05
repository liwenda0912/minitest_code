from appnium.mini_Selenium_Program.Public.conf.SqlConnectConf import Connect


def Find_sql(*loc):
    sql = "select * from uesr where name=" + loc[0] + " and id = " + loc[1] + ";"
    Connect.Cursor.execute(sql)
    result = Connect.Cursor.fetchall()
    return result


def delete_sql(*loc):
    sql = 'delete from user where name=' + loc[0] + ';'
    Connect.Cursor.execute(sql)
    result = Connect.Cursor.fetchall()
    return result


def insert_sql(*loc):
    sql = "insert into user(name,age) values(" + loc[0] + "" + loc[1] + ")"
    Connect.Cursor.execute(sql)
    result = Connect.Cursor.fetchall()
    return result


def updata_sql(loc, *args):
    sql = "update user set name=" + args[0] + ", age =" + args[0] + "where  name = " + loc + ";"
    Connect.Cursor.execute(sql)
    result = Connect.Cursor.fetchall()
    return result
