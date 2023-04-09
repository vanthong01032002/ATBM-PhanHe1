import sys
#from PySide2 import QtWidgets
from PySide2 import QtWidgets
from PySide2 import QtGui, QtCore

# from views.user_view import UserView
# from views.user_view import UserList
# from views.role_view import RoleView
from views.privileges_view import privilegesView
from views.role_view import RoleView
from views.user_view import UserList


class MainWindown():
    def __init__(self):
        super().__init__()
         # Khởi tạo đối tượng QMainWindow
        self.main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        self.main_window.setWindowTitle('Menu')
        # Thiết lập kích thước cho widget
        self.main_window.resize(700, 520)

        # Hiện thị danh sách user
        self.button_user = QtWidgets.QPushButton('Danh sách user', self.main_window)
        self.button_user.move(120,120)
        self.button_user.setFixedSize(180, 60)  # Thiết lập kích thước cố định
        # thiết lập hover cursor
        self.button_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_user.clicked.connect(self.on_click_user)

        # Hiện thị danh sách role
        self.button_role = QtWidgets.QPushButton('Danh sách role', self.main_window)
        self.button_role.move(340,120)
        self.button_role.setFixedSize(180, 60)  # Thiết lập kích thước cố định
        # thiết lập hover cursor
        self.button_role.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_role.clicked.connect(self.on_click_role)

        # Hiện thị danh sách quyền của role/user
        self.button_pri = QtWidgets.QPushButton('Danh sách quyền User/Role', self.main_window)
        self.button_pri.move(120,220)
        self.button_pri.setFixedSize(180, 60)  # Thiết lập kích thước cố định
        # thiết lập hover cursor
        self.button_pri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pri.clicked.connect(self.on_click_privileges)

        self.main_window.show()
    def on_click_user(self):
        self.main_window.close()  # hide the main window
        User_list = UserList()
        User_list.show()
    def on_click_role(self):
        self.main_window.close()  # hide the main window
        Role_view = RoleView()
        Role_view.show()
    def on_click_privileges(self):
        self.main_window.close()  # hide the main window
        privileges_View = privilegesView()
        privileges_View.show()