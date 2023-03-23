# from controllers.user_controller import UserController
from views.user_view import UserView

def main():
    # khởi tạo đối tượng UserController và UserView
    # user_controller = UserController()
    user_view = UserView()

    # sử dụng controller để lấy danh sách user
    # user_list = user_controller.get_user_list()

    # hiển thị danh sách user thông qua view

    user_view.display_user_list()
    
if __name__ == '__main__':
    main()
