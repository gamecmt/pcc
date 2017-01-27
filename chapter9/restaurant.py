# 9-1
class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening.")

restaurant = Restaurant("mid", "French")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
ak47 = Restaurant("ak47", "England")
ak47.describe_restaurant()

f117 = Restaurant("f117", "Japan")
f117.describe_restaurant()

# 9-3


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

cmt = User("chen", "mt")
cmt.describe_user()
cmt.greet_user()

# 9-4


class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening.")

    def read_number_served(self):
        print("The number served is " + str(self.number_served))

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

mid_restaurant = Restaurant("mid", "Franch")
mid_restaurant.describe_restaurant()
mid_restaurant.open_restaurant()
mid_restaurant.read_number_served()
mid_restaurant.set_number_served(5)
mid_restaurant.read_number_served()
mid_restaurant.increment_number_served(10)
mid_restaurant.read_number_served()

# 9-5


class User(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        username = self.first_name + " " + self.last_name
        print("Hello " + username)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(self.login_attempts)

cmt = User("chen", "mt")
cmt.describe_user()
cmt.greet_user()
cmt.increment_login_attempts()
cmt.read_login_attempts()
cmt.reset_login_attempts()
cmt.read_login_attempts()
