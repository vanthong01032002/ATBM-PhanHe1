import sys
from PyQt5 import QtCore, QtWidgets
# from controllers.user_controller import UserController
from views.user_view import UserView
from views.user_view import UserList
from views.role_view import RoleView

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RoleView()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
