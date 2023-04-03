class UserManagement:
    def __init__(self):
        self.users = []

    def create_user(self, user_name):
        if user_name not in self.users:
            self.users.append(user_name)

    def get_users(self):
        return self.users
    