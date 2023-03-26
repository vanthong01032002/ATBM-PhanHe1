from utils.database import connection2


class UserController:
    def get_user_list(self):
        result = connection2(
            'NhanVienQT', 'Admin123', 'SELECT * FROM ROLE_TAB_PRIVS')
        return result
