import cx_Oracle


def connection(username, password, queryString):
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
