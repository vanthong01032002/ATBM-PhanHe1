# from controllers.user_controller import UserController
from views.user_view import UserView
from views.user_view import UserList
from views.role_view import RoleView

def main():
    # khởi tạo đối tượng UserController và UserView
    # user_controller = UserController()
    # user_view = UserView()
    #role_view = RoleView()
    user_view = UserList()
    # sử dụng controller để lấy danh sách user
    # user_list = user_controller.get_user_list()

    # hiển thị danh sách user thông qua view

    # user_view.display_user_list()
    # role_view.display_role_list()
    user_view.display_user_list()
if __name__ == '__main__':
    main()
