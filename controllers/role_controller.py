from utils.database import connection


class RoleController:
    def get_role_list(self):
        result = connection(
            'NhanVienQT', 'Admin123', 'SELECT * FROM ROLE_TAB_PRIVS')
        return result

    def Add_Role(self, role_name, password):
        print("Add")

    def Recall_Role(self, role_name, table_name, privilege):
        result = connection(
            'NhanVienQT', 'Admin123', 'REVOKE {0} ON sys.{1} FROM {2}'.format(privilege, table_name, role_name))
        return result

    def Delete_Role(self, role_name):
        result = connection(
            'NhanVienQT', 'Admin123', 'DROP ROLE {0}'.format(role_name))
        return result
