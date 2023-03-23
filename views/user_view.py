import sys
from PySide2 import QtWidgets
from controllers.user_controller import UserController

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