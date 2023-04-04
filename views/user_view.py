import sys
#from PySide2 import QtWidgets
from PyQt5 import QtCore, QtWidgets
# from controllers.user_controller import UserController
from controllers.user_controller import User_Controller

class UserView:
    def display_user_list(self):
        app = QtWidgets.QApplication(sys.argv)

        user_controller = UserController()
        user_list = user_controller.get_user_list()

        # Khởi tạo đối tượng QMainWindow
        main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        main_window.setWindowTitle('My Window')

        # Khởi tạo table widget để hiển thị danh sách người dùng
        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(3)  # Đặt số lượng cột cho table widget
        table_widget.setHorizontalHeaderLabels(['GRANTEE', 'PRIVILEGE', 'TABLENAME'])

        # Thêm dữ liệu vào table widget
        for user in user_list:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(user[1])))
            table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(user[2])))

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
        main_window.resize(640,480)

        #
        user_name = QtWidgets.QLabel(main_window)
        user_name.setText("Nhập user: ")
        user_name.setStyleSheet("font-size: 16px;")

        user_name.move(410,20)

        txt_user = QtWidgets.QLineEdit(main_window)
        txt_user.setFixedWidth(160)
        txt_user.move(410,50)

        # Hiển thị widget
        main_window.show()
        # Chạy vòng lặp ứng dụng
        sys.exit(app.exec_())
    
class UserList:
    def display_user_list(self):
        app = QtWidgets.QApplication(sys.argv)
        self.user_controller = User_Controller()
        self.user_list = self.user_controller.display_user_list()
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setWindowTitle('Danh sach nguoi dung')

        self.data_Users = {"ID": "",
                           "User Name": "",
                           "Date Created": ""}

        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(['ID', 'User Name', 'Date created'])

        table_widget.selectionModel().selectionChanged.connect(self.on_sel)
        for user in self.user_list:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(user[1])))
            table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(user[2])))

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(420)
        self.scroll_area.setFixedHeight(450)
        self.scroll_area.setWidget(table_widget)
        self.main_window.setCentralWidget(self.scroll_area)

        self.main_window.resize(640,480)

        #User Name
        self.user_name = QtWidgets.QLabel(self.main_window)
        self.user_name.setText("User Name: ")
        self.user_name.setStyleSheet("font-size: 14px;")
        self.user_name.move(480,0)

        self.txt_role = QtWidgets.QLineEdit(self.main_window)
        self.txt_role.setFixedWidth(160)
        self.txt_role.setText(self.data_Users["User Name"])
        self.txt_role.move(440, 25)

        #Drop Button
        self.btn_delete = QtWidgets.QPushButton(self.main_window)
        self.btn_delete.setText("DROP USER")
        self.btn_delete.setMinimumWidth(100)
        self.btn_delete.move(470, 70)
        self.btn_delete.clicked.connect(self.Drop_User)

        #Add Button
        self.btn_delete = QtWidgets.QPushButton(self.main_window)
        self.btn_delete.setText("ADD USER")
        self.btn_delete.setMinimumWidth(100)
        self.btn_delete.move(470, 160)
        self.btn_delete.clicked.connect(self.Create_User_View)

        #Revoke Role Button
        self.btn_rRole = QtWidgets.QPushButton(self.main_window)
        self.btn_rRole.setText("Revoke Role")
        self.btn_rRole.setMinimumWidth(100)
        self.btn_rRole.move(470, 200)
        self.btn_rRole.clicked.connect(self.Revoke_Role_View)

        #Revoke Table_Privs Button
        self.btn_rTab = QtWidgets.QPushButton(self.main_window)
        self.btn_rTab.setText("Revoke Table Privs")
        self.btn_rTab.setMinimumWidth(150)
        self.btn_rTab.move(470, 240)
        self.btn_rTab.clicked.connect(self.Revoke_TabPrivs_View)
        
        #Revoke Privs Button
        self.btn_rPri = QtWidgets.QPushButton(self.main_window)
        self.btn_rPri.setText("Revoke System Privs")
        self.btn_rPri.setMinimumWidth(150)
        self.btn_rPri.move(470, 280)
        self.btn_rPri.clicked.connect(self.Revoke_Privs_View)

        #Change Password
        self.btn_change = QtWidgets.QPushButton(self.main_window)
        self.btn_change.setText("CHANGE")
        self.btn_change.setMinimumWidth(30)
        self.btn_change.move(430, 115)
        self.btn_change.clicked.connect(self.New_password)

        self.txt_change = QtWidgets.QLineEdit(self.main_window)
        self.txt_change.setFixedWidth(100)
        self.txt_change.setText("New password")
        self.txt_change.move(510, 115)
        # Hiển thị widget
        self.main_window.show()
        # Chạy vòng lặp ứng dụng
        sys.exit(app.exec_())

    def on_sel(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Users = {"ID": self.user_list[index][0],
                           "User Name": self.user_list[index][1],
                           "Date Created": self.user_list[index][2]}
            self.txt_role.setText(self.data_Users["User Name"])

    def Drop_User(self):
        self.user_controller.Drop_User(self.data_Users["User Name"])

    def New_password(self):
        self.user_controller.New_Password(self.data_Users["User Name"], self.txt_change.text())

#Create User
    def Create_User_View(self):
        self.sub_window = QtWidgets.QMainWindow()
        self.sub_window.resize(580, 400)
        self.sub_window.setWindowTitle('Them User')
        #UserName
        self.user_name = QtWidgets.QLabel(self.sub_window)
        self.user_name.setText("User Name: ")
        self.user_name.setStyleSheet("font-size: 14px;")

        self.user_name.move(150, 25)

        self.txt_user_name = QtWidgets.QLineEdit(self.sub_window)
        self.txt_user_name.setFixedWidth(160)
        self.txt_user_name.move(260, 25)

        #Password
        self.password = QtWidgets.QLabel(self.sub_window)
        self.password.setText("Password: ")
        self.password.setStyleSheet("font-size: 14px;")

        self.password.move(150, 80)

        self.txt_password = QtWidgets.QLineEdit(self.sub_window)
        self.txt_password.setFixedWidth(160)
        self.txt_password.move(260, 80)

        #Create Button
        self.btn_create = QtWidgets.QPushButton(self.sub_window)
        self.btn_create.setText("CREATE")
        self.btn_create.setMinimumWidth(30)
        self.btn_create.move(230, 140)
        self.btn_create.clicked.connect(self.Create_User)
        self.sub_window.show()

    def Create_User(self):
        self.user_controller.Create_User(self.txt_user_name.text(), self.txt_password.text())

#Revoke Role
    def Revoke_Role_View(self):

        self.sub_window = QtWidgets.QMainWindow()
        self.sub_window.setWindowTitle('USER: {0}'.format(self.txt_role.text()))
        self.user_controller1 = User_Controller()
        self.role_list = self.user_controller1.display_role_of_user(self.txt_role.text())
        self.data_Roles = {"Role": ""}
        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(6)  # Đặt số lượng cột cho table widget
        table_widget.setHorizontalHeaderLabels(['Role', 'Admin Option', 'Delegate_Option', 'Default_Role', 'Common', 'Inherited'])
        table_widget.selectionModel().selectionChanged.connect(self.on_sel1)
        for role in self.role_list:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(role[0])))
            table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(role[1])))
            table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(role[2])))
            table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(role[3])))
            table_widget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(role[4])))
            table_widget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(role[5])))
        
        # Thiết lập layout cho widget
        # Tạo khung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(420)
        self.scroll_area.setFixedHeight(450)

        # Đặt bảng trong khung cuộn
        self.scroll_area.setWidget(table_widget)

        # Đặt khung cuộn vào cửa sổ chính
        self.sub_window.setCentralWidget(self.scroll_area)

        # Thiết lập kích thước cho widget
        self.sub_window.resize(640,480)

        #Role Name
        self.role_name = QtWidgets.QLabel(self.sub_window)
        self.role_name.setText("Role Name: ")
        self.role_name.setStyleSheet("font-size: 14px;")
        self.role_name.move(480,0)

        self.txt_role1 = QtWidgets.QLineEdit(self.sub_window)
        self.txt_role1.setFixedWidth(160)
        self.txt_role1.setText(self.data_Roles["Role"])
        self.txt_role1.move(440, 25)

        #Revoke Button
        self.btn_revoke = QtWidgets.QPushButton(self.sub_window)
        self.btn_revoke.setText("REVOKE")
        self.btn_revoke.setMinimumWidth(100)
        self.btn_revoke.move(470, 70)
        self.btn_revoke.clicked.connect(self.Revoke_Role)

        self.sub_window.show()

    def Revoke_Role(self):
        print(self.txt_role.text())
        self.user_controller1.Revoke_Role_From_User(self.txt_role1.text(), self.txt_role.text())
    def on_sel1(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Roles = {"Role": self.role_list[index][0]}
            self.txt_role1.setText(self.data_Roles["Role"])
        
#Revoke Tab Privs
    def Revoke_TabPrivs_View(self):
        self.sub_window = QtWidgets.QMainWindow()
        self.sub_window.setWindowTitle('USER: {0}'.format(self.txt_role.text()))
        self.user_controller2 = User_Controller()
        self.tabprivs_list = self.user_controller2.display_tabprivs_of_user(self.txt_role.text())
        self.data_TabPrivs = {"Table_Name": "",
                           "Privilege": ""}
        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(5)  # Đặt số lượng cột cho table widget
        table_widget.setHorizontalHeaderLabels(['Owner', 'Table_Name', 'Grantor', 'Privilege', 'Grantable'])
        table_widget.selectionModel().selectionChanged.connect(self.on_sel2)
        for priv in self.tabprivs_list:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(priv[0])))
            table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(priv[1])))
            table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(priv[2])))
            table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(priv[3])))
            table_widget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(priv[4])))
        
        # Thiết lập layout cho widget
        # Tạo khung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(420)
        self.scroll_area.setFixedHeight(450)

        # Đặt bảng trong khung cuộn
        self.scroll_area.setWidget(table_widget)

        # Đặt khung cuộn vào cửa sổ chính
        self.sub_window.setCentralWidget(self.scroll_area)

        # Thiết lập kích thước cho widget
        self.sub_window.resize(640,480)

        #Table Name
        self.table_name = QtWidgets.QLabel(self.sub_window)
        self.table_name.setText("Table Name: ")
        self.table_name.setStyleSheet("font-size: 14px;")
        self.table_name.move(480,0)

        self.txt_tab = QtWidgets.QLineEdit(self.sub_window)
        self.txt_tab.setFixedWidth(160)
        self.txt_tab.setText(self.data_TabPrivs["Table_Name"])
        self.txt_tab.move(440, 25)

        #Privilege
        self.tabpriv_name = QtWidgets.QLabel(self.sub_window)
        self.tabpriv_name.setText("Privilege: ")
        self.tabpriv_name.setStyleSheet("font-size: 14px;")
        self.tabpriv_name.move(480,50)

        self.txt_tabpriv = QtWidgets.QLineEdit(self.sub_window)
        self.txt_tabpriv.setFixedWidth(160)
        self.txt_tabpriv.setText(self.data_TabPrivs["Privilege"])
        self.txt_tabpriv.move(440, 75)

        #Revoke Button
        self.btn_revoke1 = QtWidgets.QPushButton(self.sub_window)
        self.btn_revoke1.setText("REVOKE")
        self.btn_revoke1.setMinimumWidth(100)
        self.btn_revoke1.move(470, 125)
        self.btn_revoke1.clicked.connect(self.Revoke_TabPrivs)

        self.sub_window.show()

    def Revoke_TabPrivs(self):
        self.user_controller2.Revoke_TabPrivs_From_User(self.txt_tabpriv.text(), self.txt_tab.text(), self.txt_role.text())
    def on_sel2(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_TabPrivs = {"Table_Name": self.tabprivs_list[index][1],
                                  "Privilege": self.tabprivs_list[index][3]}
            self.txt_tab.setText(self.data_TabPrivs["Table_Name"])
            self.txt_tabpriv.setText(self.data_TabPrivs["Privilege"])
        
#Revoke System Privs
    def Revoke_Privs_View(self):
        self.sub_window = QtWidgets.QMainWindow()
        self.sub_window.setWindowTitle('USER: {0}'.format(self.txt_role.text()))
        self.user_controller3 = User_Controller()
        self.privs_list = self.user_controller3.display_privs_of_user(self.txt_role.text())
        self.data_Privs = {"Privilege": ""}
        table_widget = QtWidgets.QTableWidget()
        table_widget.setColumnCount(4)  # Đặt số lượng cột cho table widget
        table_widget.setHorizontalHeaderLabels(['Privilege', 'Admin_Option', 'Common', 'Inherited'])
        table_widget.selectionModel().selectionChanged.connect(self.on_sel3)
        for priv in self.privs_list:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(priv[0])))
            table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(priv[1])))
            table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(priv[2])))
            table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(priv[3])))
        
        # Thiết lập layout cho widget
        # Tạo khung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(420)
        self.scroll_area.setFixedHeight(450)

        # Đặt bảng trong khung cuộn
        self.scroll_area.setWidget(table_widget)

        # Đặt khung cuộn vào cửa sổ chính
        self.sub_window.setCentralWidget(self.scroll_area)

        # Thiết lập kích thước cho widget
        self.sub_window.resize(640,480)

        #Privilege Name
        self.pri_name = QtWidgets.QLabel(self.sub_window)
        self.pri_name.setText("Privilege Name: ")
        self.pri_name.setStyleSheet("font-size: 14px;")
        self.pri_name.move(480,0)

        self.txt_pri = QtWidgets.QLineEdit(self.sub_window)
        self.txt_pri.setFixedWidth(160)
        self.txt_pri.setText(self.data_Privs["Privilege"])
        self.txt_pri.move(440, 25)

        #Revoke Button
        self.btn_revoke2 = QtWidgets.QPushButton(self.sub_window)
        self.btn_revoke2.setText("REVOKE")
        self.btn_revoke2.setMinimumWidth(100)
        self.btn_revoke2.move(470, 75)
        self.btn_revoke2.clicked.connect(self.Revoke_Privs)

        self.sub_window.show()

    def Revoke_Privs(self):
        self.user_controller3.Revoke_Privs_From_User(self.txt_pri.text(), self.txt_role.text())
    def on_sel3(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.data_Privs = {"Privilege": self.privs_list[index][0]}
            self.txt_pri.setText(self.data_Privs["Privilege"])