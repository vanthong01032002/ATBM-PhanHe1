import utils.auth as login
from utils.database import connection2
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
class LoginController:
    def __init__(self):
        self.username_text = None
        self.password_text = None

    def login_connect(self, username_text, password_text):
        self.username_text = username_text
        self.password_text = password_text
       
        result = connection2(username_text, password_text)
        if result:
            login.myList = [username_text, password_text]
        print (login.myList)
        return result

    def get_username_and_password(self):
        return login.myList[0] , login.myList[1]