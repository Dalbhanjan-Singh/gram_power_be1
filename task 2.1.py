
import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='amc2',
                                       user='root',
                                       password='S@ini420boy')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()






sql_select_Query = "select * from user"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
#get all records
records = cursor.fetchall()