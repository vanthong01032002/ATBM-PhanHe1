import sys
import messagebox
# from PySide2 import QtWidgets
from PyQt5 import QtCore, QtWidgets

from controllers.role_controller import RoleController


class RoleView:
    def display_role_list(self):
        app = QtWidgets.QApplication(sys.argv)

        self.role_controller = RoleController()
        self.roles = self.role_controller.get_role_list()

        # Khởi tạo đối tượng QMainWindow
        self.main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        self.main_window.setWindowTitle('Danh sách role:')

        # Json data
        self.data_Roles = {"Role Name": "",
                           "Password": "",
                           "Authentication": "",
                           "Common": "",
                           "Oracle maintained": "",
                           "Inherited": "",
                           "Implicit": ""}

        # Khởi tạo table widget để hiển thị danh sách người dùng
        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(7)  # Đặt số lượng cột cho table widget
        self.table_widget.setHorizontalHeaderLabels(["Role Name",
                                                "Password",
                                                "Authentication",
                                                "Common",
                                                "Oracle maintained",
                                                "Inherited",
                                                "Implicit"])
        self.table_widget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        # Thêm dữ liệu vào table widget
        for role in self.roles:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
            self.table_widget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(role[2])))
            self.table_widget.setItem(
                row_position, 2, QtWidgets.QTableWidgetItem(str(role[3])))
            self.table_widget.setItem(
                row_position, 3, QtWidgets.QTableWidgetItem(str(role[4])))
            self.table_widget.setItem(
                row_position, 4, QtWidgets.QTableWidgetItem(str(role[5])))
            self.table_widget.setItem(
                row_position, 5, QtWidgets.QTableWidgetItem(str(role[6])))
            self.table_widget.setItem(
                row_position, 6, QtWidgets.QTableWidgetItem(str(role[7])))

        # Thiết lập layout cho widget
        # Tạo khung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(400)
        self.scroll_area.setFixedHeight(300)

        # Đặt bảng trong khung cuộn
        self.scroll_area.setWidget(self.table_widget)

        # Đặt khung cuộn vào cửa sổ chính
        self.main_window.setCentralWidget(self.scroll_area)

        # Thiết lập kích thước cho widget
        self.main_window.resize(640, 480)

        # Role Name
        self.role_name = QtWidgets.QLabel(self.main_window)
        self.role_name.setText("Role Name: ")
        self.role_name.setStyleSheet("font-size: 14px;")

        self.role_name.move(410, 0)

        self.txt_role = QtWidgets.QLineEdit(self.main_window)
        self.txt_role.setFixedWidth(160)
        self.txt_role.setText(self.data_Roles["Role Name"])
        self.txt_role.move(410, 25)

        # Password
        self.Password_name = QtWidgets.QLabel(self.main_window)
        self.Password_name.setText("Password: ")
        self.Password_name.setStyleSheet("font-size: 14px;")

        self.Password_name.move(410, 50)

        self.txt_Password = QtWidgets.QLineEdit(self.main_window)
        self.txt_Password.setFixedWidth(160)
        self.txt_Password.setText(self.data_Roles["Password"])
        self.txt_Password.move(410, 75)

        # Authentication
        self.Authentication_name = QtWidgets.QLabel(self.main_window)
        self.Authentication_name.setText("Authentication: ")
        self.Authentication_name.setStyleSheet("font-size: 14px;")

        self.Authentication_name.move(410, 100)

        self.txt_Authentication = QtWidgets.QLineEdit(self.main_window)
        self.txt_Authentication.setFixedWidth(160)
        self.txt_Authentication.setText(self.data_Roles["Authentication"])
        self.txt_Authentication.move(410, 125)

        # Common
        self.Common_name = QtWidgets.QLabel(self.main_window)
        self.Common_name.setText("Common: ")
        self.Common_name.setStyleSheet("font-size: 14px;")

        self.Common_name.move(410, 150)

        self.txt_Common = QtWidgets.QLineEdit(self.main_window)
        self.txt_Common.setFixedWidth(160)
        self.txt_Common.setText(self.data_Roles["Common"])
        self.txt_Common.move(410, 175)

        # Oracle maintained
        self.Oracle_Maintained_name = QtWidgets.QLabel(self.main_window)
        self.Oracle_Maintained_name.setText("Oracle maintained: ")
        self.Oracle_Maintained_name.setStyleSheet("font-size: 14px;")

        self.Oracle_Maintained_name.move(410, 200)

        self.txt_Oracle_Maintained = QtWidgets.QLineEdit(self.main_window)
        self.txt_Oracle_Maintained.setFixedWidth(160)
        self.txt_Oracle_Maintained.setText(
            self.data_Roles["Oracle maintained"])
        self.txt_Oracle_Maintained.move(410, 225)

        # Inherited
        self.Inherited_name = QtWidgets.QLabel(self.main_window)
        self.Inherited_name.setText("Inherited: ")
        self.Inherited_name.setStyleSheet("font-size: 14px;")

        self.Inherited_name.move(410, 250)

        self.txt_Inherited = QtWidgets.QLineEdit(self.main_window)
        self.txt_Inherited.setFixedWidth(160)
        self.txt_Inherited.setText(self.data_Roles["Inherited"])
        self.txt_Inherited.move(410, 275)

        # Implicit
        self.Implicit_name = QtWidgets.QLabel(self.main_window)
        self.Implicit_name.setText("Implicit: ")
        self.Implicit_name.setStyleSheet("font-size: 14px;")

        self.Implicit_name.move(410, 300)

        self.txt_Implicit = QtWidgets.QLineEdit(self.main_window)
        self.txt_Implicit.setFixedWidth(160)
        self.txt_Implicit.setText(self.data_Roles["Implicit"])
        self.txt_Implicit.move(410, 325)

        # Add button
        self.btn_add = QtWidgets.QPushButton(self.main_window)
        self.btn_add.setText("Thêm role")
        self.btn_add.setMinimumWidth(100)
        self.btn_add.move(30, 360)
        self.btn_add.clicked.connect(self.Add_Role)

        # Recall table button
        self.btn_recall = QtWidgets.QPushButton(self.main_window)
        self.btn_recall.setText("Thu hồi quyền bảng")
        self.btn_recall.setMinimumWidth(150)
        self.btn_recall.move(160, 360)
        self.btn_recall.clicked.connect(self.Recall_Role_Table)

        # Recall Sys button
        self.btn_recall = QtWidgets.QPushButton(self.main_window)
        self.btn_recall.setText("Thu hồi quyền hệ thống")
        self.btn_recall.setMinimumWidth(150)
        self.btn_recall.move(320, 360)
        self.btn_recall.clicked.connect(self.Recall_Role_Sys)

        # Delete button
        self.btn_delete = QtWidgets.QPushButton(self.main_window)
        self.btn_delete.setText("Xoá role")
        self.btn_delete.setMinimumWidth(100)
        self.btn_delete.move(500, 360)
        self.btn_delete.clicked.connect(self.Delete_Role)

        # Title: Thêm role

        self.title_role_create = QtWidgets.QLabel(self.main_window)
        self.title_role_create.setText("Thêm role")
        self.title_role_create.setStyleSheet("font-size: 15px;")

        self.title_role_create.move(280, 400)

        # Create role name
        self.role_name_create = QtWidgets.QLabel(self.main_window)
        self.role_name_create.setText("Role Name: ")
        self.role_name_create.setStyleSheet("font-size: 14px;")

        self.role_name_create.move(50, 410)

        self.txt_role_name_create = QtWidgets.QLineEdit(self.main_window)
        self.txt_role_name_create.setFixedWidth(160)
        self.txt_role_name_create.setText("")
        self.txt_role_name_create.move(50, 435)

        # Create role password
        self.role_password_create = QtWidgets.QLabel(self.main_window)
        self.role_password_create.setText("Role password: ")
        self.role_password_create.setStyleSheet("font-size: 14px;")

        self.role_password_create.move(450, 410)

        self.txt_role_password_create = QtWidgets.QLineEdit(self.main_window)
        self.txt_role_password_create.setFixedWidth(160)
        self.txt_role_password_create.setText("")
        self.txt_role_password_create.move(450, 435)

        # Hiển thị widget
        self.main_window.show()
        # Chạy vòng lặp ứng dụng
        sys.exit(app.exec_())

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Roles = {"Role Name": self.roles[index][0],
                               "Password": self.roles[index][2],
                               "Authentication": self.roles[index][3],
                               "Common": self.roles[index][4],
                               "Oracle maintained": self.roles[index][5],
                               "Inherited": self.roles[index][6],
                               "Implicit": self.roles[index][7]}
            self.txt_role.setText(self.data_Roles["Role Name"])
            self.txt_Password.setText(self.data_Roles["Password"])
            self.txt_Authentication.setText(self.data_Roles["Authentication"])
            self.txt_Common.setText(self.data_Roles["Common"])
            self.txt_Oracle_Maintained.setText(
                self.data_Roles["Oracle maintained"])
            self.txt_Inherited.setText(self.data_Roles["Inherited"])
            self.txt_Implicit.setText(self.data_Roles["Implicit"])
            # print('Row: {0}, Column: {1}'. format(ix.row(), ix.column()))

    def Add_Role(self):

        if self.txt_role_name_create.text() == '':
            MessageBoxErr("Lỗi", "Vui lòng nhập role name")
        else:
            result = self.role_controller.Add_Role(
                self.txt_role_name_create.text(), self.txt_role_password_create.text())
            self.roles = self.role_controller.get_role_list()
            for role in self.roles:
                row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
            self.table_widget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(role[2])))
            self.table_widget.setItem(
                row_position, 2, QtWidgets.QTableWidgetItem(str(role[3])))
            self.table_widget.setItem(
                row_position, 3, QtWidgets.QTableWidgetItem(str(role[4])))
            self.table_widget.setItem(
                row_position, 4, QtWidgets.QTableWidgetItem(str(role[5])))
            self.table_widget.setItem(
                row_position, 5, QtWidgets.QTableWidgetItem(str(role[6])))
            self.table_widget.setItem(
                row_position, 6, QtWidgets.QTableWidgetItem(str(role[7])))
            print(result)

    def Recall_Role_Table(self):
        if self.data_Roles["Role Name"] == '':
            MessageBoxErr("Lỗi", "Vui lòng chọn role, bảng hoặc quyền")
        else:
            self.main_window1 = QtWidgets.QMainWindow()

            self.main_window1.setWindowTitle('Thu hồi quyền trên bảng')

            # Json data
            self.data_Roles1 = {"Role Name": "",
                                "Password": "",
                                "Authentication": "",
                                "Common": "",
                                "Oracle maintained": "",
                                "Inherited": "",
                                "Implicit": ""}

            self.table_widget1 = QtWidgets.QTableWidget()
            self.table_widget1.setColumnCount(7)  # Đặt số lượng cột cho table widget
            self.table_widget1.setHorizontalHeaderLabels(["Role Name",
                                                    "Table Name",
                                                    "Column Name",
                                                    "Privilege",
                                                    "Grantable",
                                                    "Common",
                                                    "Inherited"])
            self.table_widget1.selectionModel().selectionChanged.connect(
                self.Change_Recall_Role_Table)

            self.roles1 = self.role_controller.get_privileged_list_of_role_table(
                self.data_Roles["Role Name"])
            if self.roles1 == []:
                MessageBoxWarn("Cảnh báo", "Role không có quyền trên bảng")
                return

            for role in self.roles1:
                row_position = self.table_widget1.rowCount()
                self.table_widget1.insertRow(row_position)
                self.table_widget1.setItem(
                    row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
                self.table_widget1.setItem(
                    row_position, 1, QtWidgets.QTableWidgetItem(str(role[2])))
                self.table_widget1.setItem(
                    row_position, 2, QtWidgets.QTableWidgetItem(str(role[3])))
                self.table_widget1.setItem(
                    row_position, 3, QtWidgets.QTableWidgetItem(str(role[4])))
                self.table_widget1.setItem(
                    row_position, 4, QtWidgets.QTableWidgetItem(str(role[5])))
                self.table_widget1.setItem(
                    row_position, 5, QtWidgets.QTableWidgetItem(str(role[6])))
                self.table_widget1.setItem(
                    row_position, 6, QtWidgets.QTableWidgetItem(str(role[7])))

            # Thiết lập layout cho widget
            # Tạo khung cuộn
            self.scroll_area1 = QtWidgets.QScrollArea()
            self.scroll_area1.setWidgetResizable(True)
            self.scroll_area1.setFixedWidth(400)
            self.scroll_area1.setFixedHeight(300)

            # Đặt bảng trong khung cuộn
            self.scroll_area1.setWidget(self.table_widget1)

            # Đặt khung cuộn vào cửa sổ chính
            self.main_window1.setCentralWidget(self.scroll_area1)

            # Thiết lập kích thước cho widget
            self.main_window1.resize(640, 480)

            # Role Name
            self.role_name_recall_table = QtWidgets.QLabel(self.main_window1)
            self.role_name_recall_table.setText("Role Name: ")
            self.role_name_recall_table.setStyleSheet("font-size: 14px;")

            self.role_name_recall_table.move(410, 0)

            self.txt_role_recall_table = QtWidgets.QLineEdit(self.main_window1)
            self.txt_role_recall_table.setFixedWidth(160)
            self.txt_role_recall_table.setText("")
            self.txt_role_recall_table.move(410, 25)

            # Table Name
            self.table_name_recall_table = QtWidgets.QLabel(self.main_window1)
            self.table_name_recall_table.setText("Table Name: ")
            self.table_name_recall_table.setStyleSheet("font-size: 14px;")

            self.table_name_recall_table.move(410, 50)

            self.txt_table_recall_table = QtWidgets.QLineEdit(self.main_window1)
            self.txt_table_recall_table.setFixedWidth(160)
            self.txt_table_recall_table.setText("")
            self.txt_table_recall_table.move(410, 75)

            # Column Name
            self.Column_name_recall_table = QtWidgets.QLabel(self.main_window1)
            self.Column_name_recall_table.setText("Column: ")
            self.Column_name_recall_table.setStyleSheet("font-size: 14px;")

            self.Column_name_recall_table.move(410, 100)

            self.txt_Column_recall_table = QtWidgets.QLineEdit(self.main_window1)
            self.txt_Column_recall_table.setFixedWidth(160)
            self.txt_Column_recall_table.setText("")
            self.txt_Column_recall_table.move(410, 125)

            # Privilege
            self.Privilege_name_recall_table = QtWidgets.QLabel(self.main_window1)
            self.Privilege_name_recall_table.setText("Privilege: ")
            self.Privilege_name_recall_table.setStyleSheet("font-size: 14px;")

            self.Privilege_name_recall_table.move(410, 150)

            self.txt_Privilege_recall_table = QtWidgets.QLineEdit(
                self.main_window1)
            self.txt_Privilege_recall_table.setFixedWidth(160)
            self.txt_Privilege_recall_table.setText("")
            self.txt_Privilege_recall_table.move(410, 175)

            # Buton: Thu hồi
            self.btn_recall1 = QtWidgets.QPushButton(self.main_window1)
            self.btn_recall1.setText("Thu hồi")
            self.btn_recall1.setMinimumWidth(100)
            self.btn_recall1.move(250, 360)
            self.btn_recall1.clicked.connect(self.Handle_Recall_Role_Table)

            self.main_window1.show()

    def Recall_Role_Sys(self):
        if self.data_Roles["Role Name"] == '':
            MessageBoxErr("Lỗi", "Vui lòng chọn role, bảng hoặc quyền")
        else:
            self.main_window2 = QtWidgets.QMainWindow()

            self.main_window2.setWindowTitle('Thu hồi quyền trên hệ thống')

            # Json data
            self.data_Roles2 = {"Role Name": "",
                                "Privilege": "",
                                "Admin option": "",
                                "Common": "",
                                "Inherited": ""}

            self.table_widget2 = QtWidgets.QTableWidget()
            self.table_widget2.setColumnCount(5)  # Đặt số lượng cột cho table widget
            self.table_widget2.setHorizontalHeaderLabels(["Role Name",
                                                    "Privilege",
                                                    "Admin option",
                                                    "Common",
                                                    "Inherited"])
            self.table_widget2.selectionModel().selectionChanged.connect(self.Change_Recall_Role_Sys)

            self.roles2 = self.role_controller.get_privileged_list_of_role_sys(
                self.data_Roles["Role Name"])
            
            if self.roles2 == []:
                MessageBoxWarn("Cảnh báo", "Role không có quyền trên hệ thống")
                return

            for role in self.roles2:
                row_position = self.table_widget2.rowCount()
                self.table_widget2.insertRow(row_position)
                self.table_widget2.setItem(
                    row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
                self.table_widget2.setItem(
                    row_position, 1, QtWidgets.QTableWidgetItem(str(role[1])))
                self.table_widget2.setItem(
                    row_position, 2, QtWidgets.QTableWidgetItem(str(role[2])))
                self.table_widget2.setItem(
                    row_position, 3, QtWidgets.QTableWidgetItem(str(role[3])))
                self.table_widget2.setItem(
                    row_position, 4, QtWidgets.QTableWidgetItem(str(role[4])))

            # Thiết lập layout cho widget
            # Tạo khung cuộn
            self.scroll_area2 = QtWidgets.QScrollArea()
            self.scroll_area2.setWidgetResizable(True)
            self.scroll_area2.setFixedWidth(400)
            self.scroll_area2.setFixedHeight(300)

            # Đặt bảng trong khung cuộn
            self.scroll_area2.setWidget(self.table_widget2)

            # Đặt khung cuộn vào cửa sổ chính
            self.main_window2.setCentralWidget(self.scroll_area2)

            # Thiết lập kích thước cho widget
            self.main_window2.resize(640, 480)

            # Role Name
            self.role_name_recall_sys = QtWidgets.QLabel(self.main_window2)
            self.role_name_recall_sys.setText("Role Name: ")
            self.role_name_recall_sys.setStyleSheet("font-size: 14px;")

            self.role_name_recall_sys.move(410, 0)

            self.txt_role_recall_sys = QtWidgets.QLineEdit(self.main_window2)
            self.txt_role_recall_sys.setFixedWidth(160)
            self.txt_role_recall_sys.setText("")
            self.txt_role_recall_sys.move(410, 25)

            # Privilege
            self.Privilege_name_recall_sys = QtWidgets.QLabel(self.main_window2)
            self.Privilege_name_recall_sys.setText("Privilege: ")
            self.Privilege_name_recall_sys.setStyleSheet("font-size: 14px;")

            self.Privilege_name_recall_sys.move(410, 50)

            self.txt_Privilege_recall_sys = QtWidgets.QLineEdit(self.main_window2)
            self.txt_Privilege_recall_sys.setFixedWidth(160)
            self.txt_Privilege_recall_sys.setText("")
            self.txt_Privilege_recall_sys.move(410, 75)

            # Button: Thu hồi
            self.btn_recall2 = QtWidgets.QPushButton(self.main_window2)
            self.btn_recall2.setText("Thu hồi")
            self.btn_recall2.setMinimumWidth(100)
            self.btn_recall2.move(250, 360)
            self.btn_recall2.clicked.connect(self.Handle_Recall_Role_Sys)

            self.main_window2.show()

    def Change_Recall_Role_Table(self, selected, deselected):
        index = -1
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Roles1 = {"Role Name": self.roles1[index][0],
                                "Table Name": self.roles1[index][2],
                                "Column Name": self.roles1[index][3],
                                "Privilege": self.roles1[index][4],
                                "Grantable": self.roles1[index][5],
                                "Common": self.roles1[index][6],
                                "Inherited": self.roles1[index][7]}
            self.txt_role_recall_table.setText(self.data_Roles1["Role Name"])
            self.txt_table_recall_table.setText(self.data_Roles1["Table Name"])
            self.txt_Column_recall_table.setText(
                self.data_Roles1["Column Name"])
            self.txt_Privilege_recall_table.setText(
                self.data_Roles1["Privilege"])

    def Change_Recall_Role_Sys(self, selected, deselected):
        index = -1
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Roles2 = {"Role Name": self.roles2[index][0],
                                "Privilege": self.roles2[index][1],
                                "Admin option": self.roles2[index][2],
                                "Common": self.roles2[index][3],
                                "Inherited": self.roles2[index][4]}
        self.txt_role_recall_sys.setText(self.data_Roles2["Role Name"])
        self.txt_Privilege_recall_sys.setText(self.data_Roles2["Privilege"])

    def Handle_Recall_Role_Table(self):
        if self.data_Roles1["Role Name"] == '' or self.data_Roles1["Table Name"] == '' or self.data_Roles1["Privilege"]:
            MessageBoxErr("Lỗi", "Vui lòng chọn role, bảng, hoặc quyền")
        else:
            result = self.role_controller.Recall_Role_Table(
                self.data_Roles1["Role Name"], self.data_Roles1["Table Name"], self.data_Roles1["Privilege"])
            
            self.roles1 = self.role_controller.get_privileged_list_of_role_table(
                self.data_Roles["Role Name"])
            if self.roles1 == []:
                MessageBoxWarn("Cảnh báo", "Role không có quyền trên bảng")
                return

            for role in self.roles1:
                row_position = self.table_widget1.rowCount()
                self.table_widget1.insertRow(row_position)
                self.table_widget1.setItem(
                    row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
                self.table_widget1.setItem(
                    row_position, 1, QtWidgets.QTableWidgetItem(str(role[2])))
                self.table_widget1.setItem(
                    row_position, 2, QtWidgets.QTableWidgetItem(str(role[3])))
                self.table_widget1.setItem(
                    row_position, 3, QtWidgets.QTableWidgetItem(str(role[4])))
                self.table_widget1.setItem(
                    row_position, 4, QtWidgets.QTableWidgetItem(str(role[5])))
                self.table_widget1.setItem(
                    row_position, 5, QtWidgets.QTableWidgetItem(str(role[6])))
                self.table_widget1.setItem(
                    row_position, 6, QtWidgets.QTableWidgetItem(str(role[7])))
            return result

    def Handle_Recall_Role_Sys(self):
        if self.data_Roles2["Role Name"] == '' or self.data_Roles2["Privilege"] == '':
            MessageBoxErr("Lỗi", "Vui lòng chọn role hoặc quyền")
        else:
            result = self.role_controller.Recall_Role_Sys(
                self.data_Roles2["Role Name"], self.data_Roles2["Privilege"])
            
            self.roles2 = self.role_controller.get_privileged_list_of_role_sys(
                self.data_Roles["Role Name"])
            
            if self.roles2 == []:
                MessageBoxWarn("Cảnh báo", "Role không có quyền trên hệ thống")
                return

            for role in self.roles2:
                row_position = self.table_widget2.rowCount()
                self.table_widget2.insertRow(row_position)
                self.table_widget2.setItem(
                    row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
                self.table_widget2.setItem(
                    row_position, 1, QtWidgets.QTableWidgetItem(str(role[1])))
                self.table_widget2.setItem(
                    row_position, 2, QtWidgets.QTableWidgetItem(str(role[2])))
                self.table_widget2.setItem(
                    row_position, 3, QtWidgets.QTableWidgetItem(str(role[3])))
                self.table_widget2.setItem(
                    row_position, 4, QtWidgets.QTableWidgetItem(str(role[4])))
            return result

    def Delete_Role(self):
        if self.data_Roles["Role Name"] == '':
            MessageBoxErr("Lỗi", "Vui lòng chọn role")
        else:
            result = self.role_controller.Delete_Role(
                self.data_Roles["Role Name"])
            print(result)


def MessageBoxErr(title, message):
    messagebox.showerror(title, message)

def MessageBoxWarn(title, message):
    messagebox.showwarning(title, message)
