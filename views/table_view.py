import sys
from PySide2 import QtWidgets
from PyQt5.QtCore import Qt

from PySide2.QtWidgets import QWidget, QDialog
from PySide2 import QtGui, QtCore
from controllers.table_controller import table_Controller
import utils.variable as value
import messagebox


class TableView:
    def __init__(self):
        super().__init__()

        self.noneOption = False
        self.grantOption = False
        self.selectOption = False
        self.insertOption = False
        self.updateOption = False
        self.deleteOption = False

        self.TableController = table_Controller()

        self.user_list = []

        self.column_selected = []

        self.search_text = ""  # Khởi tạo biến "search_text" với giá trị rỗng

        # Khởi tạo đối tượng QMainWindow
        self.main_window = QtWidgets.QMainWindow()

        # Thiết lập tiêu đề cho cửa sổ
        self.main_window.setWindowTitle('Danh sách thông tin quyền')
        # Thiết lập kích thước cho widget
        self.main_window.resize(700, 520)

        # Thiết lập p hiện thị nhập user
        self.user_name = QtWidgets.QLabel(self.main_window)
        self.user_name.setText("Nhập user/role name muốn cấp quyền : ")
        self.user_name.setStyleSheet("font-size: 16px;")
        self.user_name.adjustSize()
        self.user_name.move(410, 20)

        # Radio button for none option
        self.radioButton_none = QtWidgets.QRadioButton(self.main_window)
        self.radioButton_none.setGeometry(QtCore.QRect(410, 50, 160, 20))
        self.radioButton_none.setText("NONE")
        self.radioButton_none.toggled.connect(self.selectedNone)

        # Radio button for grant option
        self.radioButton_grant = QtWidgets.QRadioButton(self.main_window)
        self.radioButton_grant.setGeometry(QtCore.QRect(410, 80, 160, 20))
        self.radioButton_grant.setText("WITH GRANT OPTION")
        self.radioButton_grant.toggled.connect(self.selectedGrant)

        # Thiết lập ô nhập input
        self.input = QtWidgets.QLineEdit(self.main_window)
        self.input.setPlaceholderText("User name...")
        self.input.setStyleSheet("QLineEdit { padding-left: 16px; }")
        self.input.setFixedWidth(160)
        self.input.setFixedHeight(30)
        self.input.move(410, 110)

        # Thiết lập button submit
        self.btn_submit = QtWidgets.QPushButton(self.main_window)
        self.btn_submit.setFixedSize(60, 30)  # đặt kích thước là 40x40 pixel
        self.btn_submit.setStyleSheet('background-color: #999999; color: #fff')
        self.btn_submit.setText("Cấp")
        self.btn_submit.clicked.connect(self.clicked_submit)
        self.btn_submit.move(570, 110)

        # thiết lập hover cursor
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.user_list = self.TableController.display_table_list()

        # Khởi tạo table widget để hiển thị danh sách người dùng
        self.table_widget = QtWidgets.QTableWidget()
        # Đặt số lượng cột cho table widget
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['OWNER', 'TABLENAME'])

        self.table_widget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

        # Thêm dữ liệu vào table widget

        for user in self.user_list:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            self.table_widget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(user[1])))
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
        # self.btn_back.setCursor(Qt.PointingHandCursor)

        self.btn_back.clicked.connect(self.Backmenu)

    def closeWindow(self):
        self.main_window.hide()

    def showWindow(self):
        self.main_window.show()

    def selectedNone(self, selected):
        if selected:
            self.noneOption = True
            self.grantOption = False

    def selectedGrant(self, selected):
        if selected:
            self.noneOption = False
            self.grantOption = True

    def selectedInsert(self, selected):
        if selected:
            self.selectOption = False
            self.insertOption = True
            self.deleteOption = False
            self.updateOption = False

    def selectedSelect(self, selected):
        if selected:
            self.selectOption = True
            self.insertOption = False
            self.deleteOption = False
            self.updateOption = False

    def selectedUpdate(self, selected):
        if selected:
            self.selectOption = False
            self.insertOption = False
            self.deleteOption = False
            self.updateOption = True

    def selectedDelete(self, selected):
        if selected:
            self.selectOption = False
            self.insertOption = False
            self.deleteOption = True
            self.updateOption = False

    def update_user_list(self, search_text=None):
        self.user_list = self.TableController.get_user_list(search_text)
        if self.table_widget is not None:
            self.table_widget.clearContents()
            self.table_widget.setRowCount(0)
            self.table_widget.setRowCount(len(self.user_list))
            for row, user in enumerate(self.user_list):
                self.table_widget.setItem(
                    row, 0, QtWidgets.QTableWidgetItem(str(user[0])))
                self.table_widget.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(str(user[1])))
                self.table_widget.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(str(user[2])))

    def clicked_submit(self):
        if self.input.text() == '' or self.noneOption == self.grantOption:
            MessageBoxErr("Lỗi", "Vui lòng nhập đủ thông tin ")
        else:
            self.main_window1 = QtWidgets.QMainWindow()

            self.user_list1 = []

            self.user_list1 = self.TableController.get_column_name(
                self.table_selected)

            self.main_window1.setWindowTitle('Cấp quyền user trên bảng')

            # Thiết lập kích thước cho widget
            self.main_window1.resize(700, 520)

            # Khởi tạo table widget để hiển thị danh sách người dùng
            self.table_widget1 = QtWidgets.QTableWidget()
            # Đặt số lượng cột cho table widget
            self.table_widget1.setColumnCount(1)
            self.table_widget1.setHorizontalHeaderLabels(['COLUMN NAME'])
            self.table_widget1.selectionModel().selectionChanged.connect(
                self.on_selectionChanged_column)
            # Thêm dữ liệu vào table widget

            for user in self.user_list1:
                row_position = self.table_widget1.rowCount()
                self.table_widget1.insertRow(row_position)
                self.table_widget1.setItem(
                    row_position, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            # Tạo khung cuộn
            scroll_area1 = QtWidgets.QScrollArea()
            scroll_area1.setWidgetResizable(True)
            scroll_area1.setFixedWidth(390)
            scroll_area1.setFixedHeight(400)

            # Đặt bảng trong khung cuộn
            scroll_area1.setWidget(self.table_widget1)
            # # Thêm tab_widget vào QMainWindow
            self.main_window1.setCentralWidget(scroll_area1)

            # Radio button for none select
            self.radioButton_select = QtWidgets.QRadioButton(self.main_window1)
            self.radioButton_select.setGeometry(QtCore.QRect(410, 50, 160, 20))
            self.radioButton_select.setText("SELECT")
            self.radioButton_select.toggled.connect(self.selectedSelect)

            # Radio button for grant insert
            self.radioButton_insert = QtWidgets.QRadioButton(self.main_window1)
            self.radioButton_insert.setGeometry(QtCore.QRect(410, 80, 160, 20))
            self.radioButton_insert.setText("INSERT")
            self.radioButton_insert.toggled.connect(self.selectedInsert)

            # Radio button for grant update
            self.radioButton_update = QtWidgets.QRadioButton(self.main_window1)
            self.radioButton_update.setGeometry(
                QtCore.QRect(410, 110, 160, 20))
            self.radioButton_update.setText("UPDATE")
            self.radioButton_update.toggled.connect(self.selectedUpdate)

            # Radio button for grant delete
            self.radioButton_delete = QtWidgets.QRadioButton(self.main_window1)
            self.radioButton_delete.setGeometry(
                QtCore.QRect(410, 140, 160, 20))
            self.radioButton_delete.setText("DELETE")
            self.radioButton_delete.toggled.connect(self.selectedDelete)

            # Buton: Cấp
            self.btn_grant_submid = QtWidgets.QPushButton(self.main_window1)
            self.btn_grant_submid.setText("Cấp quyền")
            self.btn_grant_submid.setMinimumWidth(100)
            self.btn_grant_submid.move(250, 460)
            self.btn_grant_submid.clicked.connect(self.click_grant_submit)

            self.main_window1.show()

    def Backmenu(self):
        value.table_window.closeWindow()
        value.main_window.showWindow()

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.table_selected = self.user_list[index][1]


    def on_selectionChanged_column(self, selected, deselected):
        for ix in selected.indexes():
            index = int(format(ix.row()))
            self.column_selected.append(self.user_list1[index][0])

            alternative_color = QtGui.QColor("salmon")

            current_brush = ix.data(QtCore.Qt.BackgroundRole)
            new_brush = (
                QtGui.QBrush(alternative_color)
                if current_brush in (None, QtGui.QBrush())
                else QtGui.QBrush()
            )
            self.table_widget1.model().setData(ix, new_brush, QtCore.Qt.BackgroundRole)

    def click_grant_submit(self):
        if self.selectOption == False and self.insertOption == False and self.updateOption == False and self.deleteOption == False:
            # print(self.column_selected)
            MessageBoxErr("Lỗi", "Vui lòng chọn đủ thông tin")
        else:
            if self.selectOption:
                pri = 'select'
            elif self.insertOption:
                pri = 'insert'
            elif self.updateOption:
                pri = 'update'
            elif self.deleteOption:
                pri = 'delete'
            if self.grantOption:
                op = 'WITH GRANT OPTION'
            else:
                op = ''
            result = self.TableController.Grant_Pri(
                pri, self.input.text(), self.table_selected, op, self.column_selected)
            return result


def MessageBoxErr(title, message):
    messagebox.showerror(title, message)


def MessageBoxWarn(title, message):
    messagebox.showwarning(title, message)
