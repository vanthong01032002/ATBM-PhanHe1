from utils.database import execute_query
import utils.auth as login


class RoleController:
    def get_role_list(self):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT * FROM DBA_ROLES')
        return result

    def get_privileged_list_of_role_table(self, role_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT * FROM ROLE_TAB_PRIVS where ROLE = ' + "'{0}'".format(role_name))
        return result

    def get_privileged_list_of_role_sys(self, role_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'SELECT * FROM ROLE_ROLE_PRIVS where ROLE = ' + "'{0}'".format(role_name))
        return result

    def Add_Role(self, role_name, password):
        if password != '':
            result = execute_query(
                login.myList[0], login.myList[1], 'CREATE ROLE {0} IDENTIFIED BY {1}'.format(role_name, password))
        else:
            result = execute_query(
                login.myList[0], login.myList[1], 'CREATE ROLE {0}'.format(role_name))
        return result

    def Recall_Role_Table(self, role_name, table_name, privilege):
        result = execute_query(
            login.myList[0], login.myList[1], 'REVOKE {0} ON sys.{1} FROM {2}'.format(privilege, table_name, role_name))

        return result

    def Recall_Role_Sys(self, role_name, privilege):
        result = execute_query(
            login.myList[0], login.myList[1], 'REVOKE {0} FROM {1}'.format(privilege, role_name))
        return result

    def Delete_Role(self, role_name):
        result = execute_query(
            login.myList[0], login.myList[1], 'DROP ROLE {0}'.format(role_name))
        return result
