from utils.database import execute_query
from controllers.login_controller import LoginController

class PrivilegesController:
    def __init__(self):
        self.login_controller = LoginController()
        self.username_text = None
        self.password_text = None
        

    def get_user_list(self, search_text=None):

        self.username_text, self.password_text = self.login_controller.get_username_and_password()


        sql = "SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM dba_tab_privs"
        if search_text:
            sql += f" WHERE grantee = '{search_text}'"
        else:
            sql = "SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM dba_tab_privs"
            
        result = execute_query(self.username_text, self.password_text, sql)
            
        return result