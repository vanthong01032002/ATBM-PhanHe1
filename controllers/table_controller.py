from utils.database import execute_query
import utils.auth as login


class table_Controller:
    def display_table_list(self):
        result = execute_query(
            login.myList[0], login.myList[1], "SELECT Owner, table_name FROM all_tables WHERE table_name = '" + "NHANVIEN'")
        return result

    def Grant_Pri(self, pri, name, table, option, col):
        if (col):
            sql = ''
            for coll in col:
                sql = sql + coll + ','
            sql = sql[:-1]
        if col == '' or pri == 'insert' or pri == 'delete':
            result = execute_query(
                login.myList[0], login.myList[1], 'grant {0} on SYS.{1} to {2} {3}'.format(pri, table, name, option))
        elif (pri == 'select'):
            result = execute_query(
                login.myList[0], login.myList[1], 'select view_name from sys.all_views')
            count = 0
            while count != 10:
                for x in result:
                    if x[0] == 'UV_{0}{1}'.format(table, count):
                        print("i found it!")
                        break
                count = count + 1
            result = execute_query(
                login.myList[0], login.myList[1], 'create view UV_{0}{1} as select {2} from sys.{0}'.format(table, count, sql))
            result = execute_query(
                login.myList[0], login.myList[1], 'grant {0} on UV_{0}{1} to {3} {4}'.format(pri, col, table, name, option))
        elif (pri == 'update'):
            result = execute_query(
                login.myList[0], login.myList[1], 'grant {0}({1}) on SYS.{2} to {3} {4}'.format(pri, sql, table, name, option))
        return result

    def get_column_name(self, table):
        result = execute_query(
            login.myList[0], login.myList[1], "SELECT column_name FROM all_tab_cols WHERE table_name = upper('" + table + "')")
        return result
