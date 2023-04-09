import sys       
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QMessageBox, QDialog
import messagebox
from PySide2 import QtGui, QtCore
from controllers.login_controller import LoginController
from views.menu_views import MainWindown

import utils.variable as value

class LoginWindow:
    def __init__(self):
        self.login_controllers = LoginController()
        self.login_window = QtWidgets.QMainWindow()
        global myList
        myList = []

         # Thiết lập tiêu đề cho cửa sổ
        self.login_window.setWindowTitle('login')
        
         # Thiết lập kích thước cho widget
        self.login_window.resize(640,480)

        #   Thiết lập ô hiện thị nhập username
        user_name = QLabel(self.login_window)
        user_name.setText("Nhập username: ")
        user_name.setStyleSheet("font-size: 14px;")
        user_name.move(250,20)

        # Thiết lập ô nhập input username
        self.username_input = QLineEdit(self.login_window)
        self.username_input.setPlaceholderText("user name")
        self.username_input.setStyleSheet("QLineEdit { padding-left: 20px; }")
        self.username_input.setFixedWidth(160)
        self.username_input.move(250,60)

        #   Thiết lập ô hiện thị nhập password
        password = QLabel(self.login_window)
        password.setText("Nhập password: ")
        password.setStyleSheet("font-size: 14px;")
        password.move(250,110)

        # Thiết lập ô nhập input password
        self.password_input = QLineEdit(self.login_window)
        self.password_input.setPlaceholderText("password")
        self.password_input.setStyleSheet("QLineEdit { padding-left: 20px; }")
        self.password_input.setFixedWidth(160)
        self.password_input.move(250,150)
        self.password_input.setEchoMode(QLineEdit.Password)

        #  Thiết lập button login
        btn_login = QPushButton(self.login_window)
        btn_login.setFixedSize(60,30)  # đặt kích thước là 40x40 pixel
        btn_login.setStyleSheet('background-color: #3450D9; color: #fff')
        btn_login.setText("Login")
        btn_login.clicked.connect(self.clicked_login)
        btn_login.move(300, 190)
        # thiết lập hover cursor
        btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        # Hiển thị cửa sổ đăng nhập
        self.login_window.show()
    
        
    def clicked_login(self):
        self.user_name_text = self.username_input.text()
        self.password_text = self.password_input.text()
        result =self.login_controllers.login_connect(self.user_name_text, self.password_text)
        if result:
            MessageBoxInfo("Dang nhap", "Thanh cong")
            value.login_window.closeWindow()
            # Đăng nhập thành công, chuyển qua trang menu
            value.main_window = MainWindown()
            value.main_window.showWindow()
        else:
            MessageBoxErr("Dang nhap", "That Bai")
    def closeWindow(self):
        self.login_window.hide()
    def showWindow(self):
        self.login_window.show()
            

def MessageBoxInfo(title, message):
    messagebox.showinfo(title, message)
        

def MessageBoxErr(title, message):
    messagebox.showerror(title, message)

            





            
