import sys
import cx_Oracle


def connection1(username, password, queryString):
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

oracle_client_initialized = False

def initialize_oracle_client(lib_dir):
    global oracle_client_initialized
    if not oracle_client_initialized:
        try:
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
            oracle_client_initialized = True
        except Exception as err:
            print("Error initializing Oracle Client:", err)
            sys.exit(1)

def connection2(username, password):
    #lib_dir = r"C:\oclient\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    lib_dir = r"D:\Download\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    initialize_oracle_client(lib_dir)
    
    try:
        con = cx_Oracle.connect(username, password, 'localhost:1521/XEPDB1')
        return con.cursor()

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
        return False

    except Exception as er:
        print('Error:'+str(er))
        return False


def execute_query(username, password, query_string):
    cursor = connection2(username, password)
    if cursor:
        try:
            cursor.execute(query_string)
            result = cursor.fetchall()
            cursor.close()
            return result
        except cx_Oracle.DatabaseError as er:
            print('There is an error in the Oracle database:', er)
            cursor.close()
            return False
    else:
        return False
