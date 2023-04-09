from utils.database import execute_query
import utils.auth as login


class pri_Controller:
    def display_table_list(self):
        result = execute_query(
            login.myList[0], login.myList[1], "select privilege from dba_sys_privs where grantee = 'DBA'")
        return result

    def Grant_Pri(self, name, user):
        result = execute_query(
            login.myList[0], login.myList[1], 'grant {0} to {1}'.format(name, user))
        return result