import sys
import cx_Oracle


def execute_query(username, password, queryString):
    try:
        con = cx_Oracle.connect(username, password, 'localhost:1521/XEPDB1')

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)

    else:
        try:
            cur = con.cursor()

            # fetchall() is used to fetch all records from result set
            cur.execute(queryString)
            rows = cur.fetchall()
            if cur:
                cur.close()
            return rows

        except cx_Oracle.DatabaseError as er:
            print('There is an error in the Oracle database:', er)
            if cur:
                cur.close()
            return False

        except Exception as er:
            print('Error:'+str(er))
            if cur:
                cur.close()
            return False

def connection2(username, password):
    # lib_dir = r"D:\Download\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"    
    try:
        con = cx_Oracle.connect(username, password, 'localhost:1521/XEPDB1')
        return con

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
        return False

    except Exception as er:
        print('Error:'+str(er))
        return False