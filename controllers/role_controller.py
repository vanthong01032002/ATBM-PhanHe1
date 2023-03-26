from utils.database import connection


class RoleController:
    def get_role_list(self):
        result = connection(
            'NhanVienQT', 'Admin123', 'SELECT * FROM DBA_ROLES')
        return result

    def get_privileged_list_of_role_table(self, role_name):
        result = connection(
            'NhanVienQT', 'Admin123', 'SELECT * FROM ROLE_TAB_PRIVS where ROLE = ' + "'{0}'".format(role_name))
        return result

    def get_privileged_list_of_role_sys(self, role_name):
        result = connection(
            'NhanVienQT', 'Admin123', 'SELECT * FROM ROLE_ROLE_PRIVS where ROLE = ' + "'{0}'".format(role_name))
        return result

    def Add_Role(self, role_name, password):
        if password != '':
            result = connection(
                'NhanVienQT', 'Admin123', 'CREATE ROLE {0} IDENTIFIED BY {1}'.format(role_name, password))
        else:
            result = connection(
                'NhanVienQT', 'Admin123', 'CREATE ROLE {0}'.format(role_name))
        return result

    def Recall_Role_Table(self, role_name, table_name, privilege):
        result = connection(
            'NhanVienQT', 'Admin123', 'REVOKE {0} ON sys.{1} FROM {2}'.format(privilege, table_name, role_name))

        return result

    def Recall_Role_Sys(self, role_name, privilege):
        result = connection(
            'NhanVienQT', 'Admin123', 'REVOKE {0} FROM {1}'.format(privilege, role_name))
        return result

    def Delete_Role(self, role_name):
        result = connection(
            'NhanVienQT', 'Admin123', 'DROP ROLE {0}'.format(role_name))
        return result
