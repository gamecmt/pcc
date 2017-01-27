class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla']

    def read_list(self):
        print(self.flavors)

icecreamstand = IceCreamStand("mid", "French")
icecreamstand.open_restaurant()
icecreamstand.read_list()

print("************")

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

    # def show_privileges(self):
    #     print(self.privileges)

cmt = Admin("chen", "mt")
cmt.privileges.show_privileges()

# 9-8

