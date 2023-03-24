from utils.database import connection


class UserController:
    def get_user_list(self):
        result = connection(
            'NhanVienQT', 'Admin123', 'SELECT * FROM ROLE_TAB_PRIVS')
        return result
