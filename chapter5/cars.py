cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 5-1
car = "bmw"
print("Is car == 'BMW'? I predict True.")
print(car == 'bmw')

print("\nIs car == 'audi'? Ipredict False.")
print(car == 'audi')

# 5-2
a = 'test'
b = 'just'

print(a == b)
print(a != b)

age = 19
if age >= 18:
    print("You are old enough to vote!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 5-3
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("you won 5.")

# 5-4
if 'green' in alien_color:
    print("you won 5.")
else:
    print("you won 10.")

# 5-5
if 'green' in alien_color:
    print("you won 5.")
elif:
    print("you won 10.")