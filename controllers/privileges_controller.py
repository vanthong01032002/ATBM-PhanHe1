from utils.database import execute_query
import utils.auth as login

class PrivilegesController:

    def get_user_list(self, search_text=None):

        sql = "SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM dba_tab_privs"
        if search_text:
            sql += f" WHERE grantee = '{search_text}' FETCH FIRST 500 ROWS ONLY"
        else:
            sql = "SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM dba_tab_privs FETCH FIRST 500 ROWS ONLY"
            
        result = execute_query(login.myList[0], login.myList[1], sql)
            
        return result