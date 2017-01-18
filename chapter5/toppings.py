requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5-8
users = ['admin', 'jack', 'tom', 'simth', 'coliton']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")

print("******************")
# 5-9
users = []
if not users:
    print("We need to find some users!")
else:
    for user in users:        
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")

# 5-10
current_users=['admin','ak47','f117','cmt','peiandsky','flypig']
new_users=['laohu','jiaji','hao','ak47','f117']
for new_user in new_users:
    if new_user in current_users:
        print("The name "+new_user+" was used, please choose another.")
    else:
        print("The name "+new_user+" is not used.")

# 5-11
nums=list(range(1,10))
for num in nums:
    if num==1:
        print("1st")
    elif num==2:
        print("2nd")
    elif num==3:
        print("3rd")
    else:
        print(str(num)+"th")