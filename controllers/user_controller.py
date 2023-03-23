from utils.database import connection

class UserController:
    def get_user_list(self):
        cursor = connection.cursor()
        cursor.execute('SELECT grantee, privilege, table_name FROM dba_tab_privs')
        user_list = cursor.fetchall()
        connection.close()
        return user_list