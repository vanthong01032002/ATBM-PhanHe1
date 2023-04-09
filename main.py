import sys
import cx_Oracle
from PyQt5 import QtCore, QtWidgets
from utils.auth import LoginWindow
import utils.variable as value

def main():
    #lib_dir = r"C:\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    # lib_dir = "C:\oclient\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
    # global oracle_client_initialized
    # oracle_client_initialized = False
    # if not oracle_client_initialized:
    #     try:
    #         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    #         oracle_client_initialized = True
    #     except Exception as err:
    #         print("Error initializing Oracle Client:", err)
    #         sys.exit(1)

    app = QtWidgets.QApplication(sys.argv)
    # main_windown = MainWindown()
    value.login_window = LoginWindow()

    sys.exit(app.exec_())
    # window = RoleView()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
