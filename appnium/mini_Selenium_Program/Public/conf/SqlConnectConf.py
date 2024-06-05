import pymysql


class Connect:
    # noinspection PyBroadException
    try:
        connection = pymysql.Connection(
            host="localhost",
            user="root",
            password="root",
            database="yourdatabase"
        )
        Cursor = connection.cursor()
    except Exception:
        print(Exception)
    except ConnectionRefusedError:
        print(ConnectionRefusedError)
    except ConnectionError:
        print(ConnectionError)
