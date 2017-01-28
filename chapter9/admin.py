class Privileges(object):

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


class User(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        username = self.first_name + " " + self.last_name
        print("Hello " + username)


class Admin(User):

    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)

