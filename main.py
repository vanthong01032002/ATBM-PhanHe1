import sys
from PyQt5 import QtCore, QtWidgets
# from controllers.user_controller import UserController
# from views.user_view import UserView
# from views.user_view import UserList
# from views.role_view import RoleView
# from views.menu_views import MainWindown
from utils.auth import LoginWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    # main_windown = MainWindown()
    Login_Window =LoginWindow()

    sys.exit(app.exec_())
    # window = RoleView()
    # sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
