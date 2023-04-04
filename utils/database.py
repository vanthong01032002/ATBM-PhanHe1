import sys
import cx_Oracle


def connection1(username, password, queryString):
    try:
        con = cx_Oracle.connect(username, password, 'localhost:1521/ORCLPDB')

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


def connection2(username, password, queryString):
    lib_dir = r"C:\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    try:
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    except Exception as err:
        print("Error connecting: cx_Oracle.init_oracle_client()")
        print(err)
        sys.exit(1)
    connection = cx_Oracle.connect('C##ADMIN/1234@localhost:1521/xe')


def connection3(username, password, queryString):
    lib_dir = r"C:\oclient\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    try:
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    except Exception as err:
        print("Error connecting: cx_Oracle.init_oracle_client()")
        print(err)
        sys.exit(1)
    con = cx_Oracle.connect(username, password, 'localhost:1521/XEPDB1')
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
