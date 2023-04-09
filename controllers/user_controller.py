from utils.database import connection2
from utils.database import execute_query
import utils.auth as login

class User_Controller:
    def display_user_list(self):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT USER_ID, USERNAME, CREATED FROM ALL_USERS')
        return result
    
    def Drop_User(self, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'DROP USER {0}'.format(user_name))
        return result
    
    def New_Password(self, user_name, newpassword):
        result = execute_query(
            login.myList[0], login.myList[1], 'ALTER USER {0} IDENTIFIED BY {1}'.format(user_name, newpassword))
        return result
    
    def Create_User(self, user_name, password):
        result = execute_query(
            login.myList[0], login.myList[1], 'CREATE USER {0} IDENTIFIED BY {1}'.format(user_name, password))
        return result
    
    def display_role_of_user(self, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT granted_role, admin_option, delegate_option, default_role, common, inherited FROM SYS.DBA_ROLE_PRIVS WHERE grantee = ' + "'{0}'".format(user_name))
        return result
    
    def Revoke_Role_From_User(self, role_name, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'REVOKE {0} FROM {1}'.format(role_name, user_name))
        return result
    
    def display_tabprivs_of_user(self, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT owner, table_name, grantor, privilege, grantable FROM SYS.DBA_TAB_PRIVS WHERE grantee = ' + "'{0}'".format(user_name))
        return result
    
    def Revoke_TabPrivs_From_User(self, pri_name, table_name, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'REVOKE {0} ON {1} FROM {2}'.format(pri_name, table_name, user_name))
        return result
    
    def display_privs_of_user(self, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT privilege, admin_option, common, inherited FROM SYS.DBA_SYS_PRIVS WHERE grantee = ' + "'{0}'".format(user_name))
        return result
    
    def Revoke_Privs_From_User(self, pri_name, user_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'REVOKE {0} FROM {1}'.format(pri_name, user_name))
        return result
    
