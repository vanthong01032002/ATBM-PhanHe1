import sys
from PySide2 import QtWidgets
from PyQt5.QtCore import Qt

from PySide2.QtWidgets import QWidget, QDialog
from PySide2 import QtGui, QtCore
from controllers.pri_controller import pri_Controller
import utils.variable as value
import messagebox


class PriView:
    def __init__(self):
        super().__init__()

        self.TableController = pri_Controller()

        self.user_list = []

        self.search_text = ""  # Khởi tạo biến "search_text" với giá trị rỗng

        # Khởi tạo đối tượng QMainWindow
        self.main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        self.main_window.setWindowTitle('Danh sách quyền')
        # Thiết lập kích thước cho widget
        self.main_window.resize(700, 520)

        # Thiết lập p hiện thị nhập user
        self.user_name = QtWidgets.QLabel(self.main_window)
        self.user_name.setText("Nhập user/role name muốn cấp quyền : ")
        self.user_name.setStyleSheet("font-size: 16px;")
        self.user_name.adjustSize()
        self.user_name.move(410, 20)

        # Thiết lập ô nhập input
        self.input = QtWidgets.QLineEdit(self.main_window)
        self.input.setPlaceholderText("User name...")
        self.input.setStyleSheet("QLineEdit { padding-left: 16px; }")
        self.input.setFixedWidth(160)
        self.input.setFixedHeight(30)
        self.input.move(410, 60)

        # Thiết lập button submit
        self.btn_submit = QtWidgets.QPushButton(self.main_window)
        self.btn_submit.setFixedSize(60, 30)  # đặt kích thước là 40x40 pixel
        self.btn_submit.setStyleSheet('background-color: #999999; color: #fff')
        self.btn_submit.setText("Cấp")
        self.btn_submit.clicked.connect(self.clicked_submit)
        self.btn_submit.move(570, 60)

        # thiết lập hover cursor
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.user_list = self.TableController.display_table_list()

        # Khởi tạo table widget để hiển thị danh sách người dùng
        self.table_widget = QtWidgets.QTableWidget()
        # Đặt số lượng cột cho table widget
        self.table_widget.setColumnCount(1)
        self.table_widget.setHorizontalHeaderLabels(['PRIVILEGES'])

        self.table_widget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

        # Thêm dữ liệu vào table widget

        for user in self.user_list:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
        # Tạo khung cuộn
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(390)
        scroll_area.setFixedHeight(400)

        # Đặt bảng trong khung cuộn
        scroll_area.setWidget(self.table_widget)
        # # Thêm tab_widget vào QMainWindow
        self.main_window.setCentralWidget(scroll_area)

        # Thiết lập button back
        self.btn_back = QtWidgets.QPushButton(self.main_window)
        self.btn_back.setFixedSize(60, 30)  # đặt kích thước là 40x40 pixel
        self.btn_back.setStyleSheet('background-color: #3450D9; color: #fff')
        self.btn_back.setText("BACK")
        self.btn_back.move(610, 470)
        self.btn_back.clicked.connect(self.Backmenu)

    def closeWindow(self):
        self.main_window.hide()

    def showWindow(self):
        self.main_window.show()

    def clicked_submit(self):
        if self.input.text() == '':
            MessageBoxErr("Lỗi", "Vui lòng nhập đủ thông tin ")
        else:
            result = self.TableController.Grant_Pri(self.table_selected, self.input.text())
            return result
    def Backmenu(self):
        value.pri_window.closeWindow()
        value.main_window.showWindow()

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.table_selected = self.user_list[index][0]

def MessageBoxErr(title, message):
    messagebox.showerror(title, message)


def MessageBoxWarn(title, message):
    messagebox.showwarning(title, message)
