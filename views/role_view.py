import sys
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QPushButton

from controllers.role_controller import RoleController


class RoleView:
    def display_role_list(self):
        app = QtWidgets.QApplication(sys.argv)

        self.role_controller = RoleController()
        self.roles = self.role_controller.get_role_list()

        # Khởi tạo đối tượng QMainWindow
        main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        main_window.setWindowTitle('My Window')

        # Json data
        self.data_Roles = {"Role Name": "",
                           "Table Name": "",
                           "Column Name": "",
                           "Privilege": "",
                           "Grantable": "",
                           "Common": "",
                           "Inherited": ""}

        # Khởi tạo table widget để hiển thị danh sách người dùng
        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(7)  # Đặt số lượng cột cho table widget
        table_widget.setHorizontalHeaderLabels(["Role Name",
                                                "Table Name",
                                                "Column Name",
                                                "Privilege",
                                                "Grantable",
                                                "Common",
                                                "Inherited",])
        table_widget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        # Thêm dữ liệu vào table widget
        for role in self.roles:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
            table_widget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(role[2])))
            table_widget.setItem(
                row_position, 2, QtWidgets.QTableWidgetItem(str(role[3])))
            table_widget.setItem(
                row_position, 3, QtWidgets.QTableWidgetItem(str(role[4])))
            table_widget.setItem(
                row_position, 4, QtWidgets.QTableWidgetItem(str(role[5])))
            table_widget.setItem(
                row_position, 5, QtWidgets.QTableWidgetItem(str(role[6])))
            table_widget.setItem(
                row_position, 6, QtWidgets.QTableWidgetItem(str(role[7])))

        # Thiết lập layout cho widget
        # Tạo khung cuộn
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(400)
        scroll_area.setFixedHeight(300)

        # Đặt bảng trong khung cuộn
        scroll_area.setWidget(table_widget)

        # Đặt khung cuộn vào cửa sổ chính
        main_window.setCentralWidget(scroll_area)

        # Thiết lập kích thước cho widget
        main_window.resize(640, 480)

        # Role Name
        self.role_name = QtWidgets.QLabel(main_window)
        self.role_name.setText("Role Name: ")
        self.role_name.setStyleSheet("font-size: 14px;")

        self.role_name.move(410, 0)

        self.txt_role = QtWidgets.QLineEdit(main_window)
        self.txt_role.setFixedWidth(160)
        self.txt_role.setText(self.data_Roles["Role Name"])
        self.txt_role.move(410, 25)

        # Table Name
        self.table_name = QtWidgets.QLabel(main_window)
        self.table_name.setText("Table Name: ")
        self.table_name.setStyleSheet("font-size: 14px;")

        self.table_name.move(410, 50)

        self.txt_table = QtWidgets.QLineEdit(main_window)
        self.txt_table.setFixedWidth(160)
        self.txt_table.setText(self.data_Roles["Table Name"])
        self.txt_table.move(410, 75)

        # Column Name
        self.column_name = QtWidgets.QLabel(main_window)
        self.column_name.setText("Column Name: ")
        self.column_name.setStyleSheet("font-size: 14px;")

        self.column_name.move(410, 100)

        self.txt_column = QtWidgets.QLineEdit(main_window)
        self.txt_column.setFixedWidth(160)
        self.txt_column.setText(self.data_Roles["Column Name"])
        self.txt_column.move(410, 125)

        # Privilege
        self.privilege_name = QtWidgets.QLabel(main_window)
        self.privilege_name.setText("Privilege: ")
        self.privilege_name.setStyleSheet("font-size: 14px;")

        self.privilege_name.move(410, 150)

        self.txt_privilege = QtWidgets.QLineEdit(main_window)
        self.txt_privilege.setFixedWidth(160)
        self.txt_privilege.setText(self.data_Roles["Privilege"])
        self.txt_privilege.move(410, 175)

        # Grantable
        self.grantable_name = QtWidgets.QLabel(main_window)
        self.grantable_name.setText("Grantable: ")
        self.grantable_name.setStyleSheet("font-size: 14px;")

        self.grantable_name.move(410, 200)

        self.txt_grantable = QtWidgets.QLineEdit(main_window)
        self.txt_grantable.setFixedWidth(160)
        self.txt_grantable.setText(self.data_Roles["Grantable"])
        self.txt_grantable.move(410, 225)

        # Common
        self.common_name = QtWidgets.QLabel(main_window)
        self.common_name.setText("Common: ")
        self.common_name.setStyleSheet("font-size: 14px;")

        self.common_name.move(410, 250)

        self.txt_common = QtWidgets.QLineEdit(main_window)
        self.txt_common.setFixedWidth(160)
        self.txt_common.setText(self.data_Roles["Common"])
        self.txt_common.move(410, 275)

        # Inherited
        self.inherited_name = QtWidgets.QLabel(main_window)
        self.inherited_name.setText("Inherited: ")
        self.inherited_name.setStyleSheet("font-size: 14px;")

        self.inherited_name.move(410, 300)

        self.txt_inherited = QtWidgets.QLineEdit(main_window)
        self.txt_inherited.setFixedWidth(160)
        self.txt_inherited.setText(self.data_Roles["Inherited"])
        self.txt_inherited.move(410, 325)

        # Add button
        self.btn_add = QtWidgets.QPushButton(main_window)
        self.btn_add.setText("Thêm role")
        self.btn_add.setMinimumWidth(100)
        self.btn_add.move(100, 360)
        self.btn_add.clicked.connect(self.Add_Role)

        # Recall button
        self.btn_recall = QtWidgets.QPushButton(main_window)
        self.btn_recall.setText("Thu hồi quyền")
        self.btn_recall.setMinimumWidth(100)
        self.btn_recall.move(250, 360)
        self.btn_recall.clicked.connect(self.Recall_Role)

        # Delete button
        self.btn_delete = QtWidgets.QPushButton(main_window)
        self.btn_delete.setText("Xoá role")
        self.btn_delete.setMinimumWidth(100)
        self.btn_delete.move(400, 360)
        self.btn_delete.clicked.connect(self.Delete_Role)

        # Title: Thêm role

        self.title_role_create = QtWidgets.QLabel(main_window)
        self.title_role_create.setText("Thêm role")
        self.title_role_create.setStyleSheet("font-size: 15px;")

        self.title_role_create.move(280, 400)

        # Create role name
        self.role_name_create = QtWidgets.QLabel(main_window)
        self.role_name_create.setText("Role Name: ")
        self.role_name_create.setStyleSheet("font-size: 14px;")

        self.role_name_create.move(50, 410)

        self.txt_role_name_create = QtWidgets.QLineEdit(main_window)
        self.txt_role_name_create.setFixedWidth(160)
        self.txt_role_name_create.setText("")
        self.txt_role_name_create.move(50, 435)

        # Create role password
        self.role_password_create = QtWidgets.QLabel(main_window)
        self.role_password_create.setText("Role password: ")
        self.role_password_create.setStyleSheet("font-size: 14px;")

        self.role_password_create.move(450, 410)

        self.txt_role_password_create = QtWidgets.QLineEdit(main_window)
        self.txt_role_password_create.setFixedWidth(160)
        self.txt_role_password_create.setText("")
        self.txt_role_password_create.move(450, 435)

        # Hiển thị widget
        main_window.show()
        # Chạy vòng lặp ứng dụng
        sys.exit(app.exec_())

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Roles = {"Role Name": self.roles[index][0],
                               "Table Name": self.roles[index][2],
                               "Column Name": self.roles[index][3],
                               "Privilege": self.roles[index][4],
                               "Grantable": self.roles[index][5],
                               "Common": self.roles[index][6],
                               "Inherited": self.roles[index][7]}
            self.txt_role.setText(self.data_Roles["Role Name"])
            self.txt_table.setText(self.data_Roles["Table Name"])
            self.txt_column.setText(self.data_Roles["Column Name"])
            self.txt_privilege.setText(self.data_Roles["Privilege"])
            self.txt_grantable.setText(self.data_Roles["Grantable"])
            self.txt_common.setText(self.data_Roles["Common"])
            self.txt_inherited.setText(self.data_Roles["Inherited"])
            # print('Row: {0}, Column: {1}'. format(ix.row(), ix.column()))

    def Add_Role(self):
        print("Add")

    def Recall_Role(self):
        result = self.role_controller.Recall_Role(
            self.data_Roles["Role Name"],
            self.data_Roles["Table Name"],
            self.data_Roles["Privilege"])
        print(result)

    def Delete_Role(self):
        result = self.role_controller.Delete_Role(self.data_Roles["Role Name"])
        print(result)
