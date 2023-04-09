import sys
import cx_Oracle
from PyQt5 import QtCore, QtWidgets
# from controllers.user_controller import UserController
# from views.user_view import UserView
# from views.user_view import UserList
# from views.role_view import RoleView
# from views.menu_views import MainWindown
from utils.auth import LoginWindow

def main():
    lib_dir = r"C:\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"

    global oracle_client_initialized
    oracle_client_initialized = False
    if not oracle_client_initialized:
        try:
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
            oracle_client_initialized = True
        except Exception as err:
            print("Error initializing Oracle Client:", err)
            sys.exit(1)

    
    app = QtWidgets.QApplication(sys.argv)
    # main_windown = MainWindown()
    Login_Window =LoginWindow()
    

    sys.exit(app.exec_())
    # window = RoleView()
    # sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
