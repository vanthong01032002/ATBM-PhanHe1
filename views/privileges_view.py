import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from PySide2 import QtGui, QtCore
from controllers.privileges_controller import PrivilegesController

class privilegesView:
    def __init__(self):
        super().__init__()
    
        self.PrivilegesController = PrivilegesController()

        self.user_list = []
        
        self.search_text = ""  # Khởi tạo biến "search_text" với giá trị rỗng

        # Khởi tạo đối tượng QMainWindow
        self.main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        self.main_window.setWindowTitle('Danh sách thông tin quyền')
        # Thiết lập kích thước cho widget
        self.main_window.resize(700, 520)
        
        # Thiết lập p hiện thị nhập user
        self.user_name = QtWidgets.QLabel(self.main_window)
        self.user_name.setText("Nhập user/role : ")
        self.user_name.setStyleSheet("font-size: 16px;")
        self.user_name.adjustSize()
        self.user_name.move(410,20)

        # Thiết lập ô nhập input
        self.search_bar = QtWidgets.QLineEdit(self.main_window)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet("QLineEdit { padding-left: 16px; }")
        self.search_bar.setFixedWidth(160)
        self.search_bar.setFixedHeight(30)
        self.search_bar.move(410, 60)

        #Thiết lập button search
        self.btn_search = QtWidgets.QPushButton(self.main_window)
        self.btn_search.setFixedSize(60,30)  # đặt kích thước là 40x40 pixel
        self.btn_search.setStyleSheet('background-color: #999999; color: #fff')
        self.btn_search.setText("Search")
        self.btn_search.clicked.connect(self.clicked_search)
        self.btn_search.move(570,60)
        
        # thiết lập hover cursor
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    
        # thiết lập button xem tất cả
        self.btn_all = QtWidgets.QPushButton(self.main_window)
        self.btn_all.setFixedSize(60,30)  # đặt kích thước là 40x40 pixel
        self.btn_all.setStyleSheet('background-color: #999999; color: #fff')
        self.btn_all.setText('All')
        # cỡ chữ cho text all trong button
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_all.setFont(font)

        self.btn_all.clicked.connect(self.clicked_btn)
        self.btn_all.move(470,140)
        # thiết lập hover cursor
        self.btn_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.user_list = self.PrivilegesController.get_user_list(self.search_text)

            # Khởi tạo table widget để hiển thị danh sách người dùng
        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(3)  # Đặt số lượng cột cho table widget
        self.table_widget.setHorizontalHeaderLabels(['GRANTEE', 'PRIVILEGE', 'TABLENAME'])
        # Thêm dữ liệu vào table widget

        for user in self.user_list:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(user[1])))
            self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(user[2])))
        # Tạo khung cuộn
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(390)
        scroll_area.setFixedHeight(400)

        # Đặt bảng trong khung cuộn
        scroll_area.setWidget(self.table_widget)
        # # Thêm tab_widget vào QMainWindow
        self.main_window.setCentralWidget(scroll_area)
        self.main_window.show()

        
    def update_user_list(self, search_text=None):
        self.user_list = self.PrivilegesController.get_user_list(search_text)
        if self.table_widget is not None:
            self.table_widget.clearContents()
            self.table_widget.setRowCount(0)
            self.table_widget.setRowCount(len(self.user_list))
            for row, user in enumerate(self.user_list):
                self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[0])))
                self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(user[1])))
                self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(user[2])))
    def clicked_search(self):
        self.search_text = self.search_bar.text()
        self.update_user_list(self.search_text)

    def clicked_btn(self):
        self.search_text = None
        self.update_user_list(self.search_text)
