#--coding=utf8--
# input在输入数据的时候必须用引号
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you?")

# height = input("How tall are you, in inches?")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

# # 7-1
# car = input("Which car are you choose?")
# print("Let me see if I can find you a " + car + ".")

# # 7-2
# num = input("How many people in dinner?")
# num = int(num)
# if num > 8:
#     print("I'm sorry, no tables")
# else:
#     print("Yes, have a good dinner.")

# # 7-3
# num = input("Enter a number:")
# num = int(num)
# if num % 10 == 0:
#     print(num + " can exact division!")
# else:
#     print(num + " can not exact division!")

# # 7-4
# prompt = "\nPlease enter the pizza toppings： "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     message = raw_input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print("We will add " + message + "in the pizza toppings.")

# # 7-5
# prompt = "\nPlease enter your age： "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     age = raw_input(prompt)

#     if age == 'quit':
#         break
#     else:
#         if int(age) < 3:
#             print("You are baby, you can free watch.")
#         elif 3 <= int(age) <= 12:
#             print("You are boy, the tickt 10 dollar.")
#         elif int(age) > 12:
#             print("The tickt 15 dallar.")

# # 7-6
# # 7-7
# # 7-8
# sandwich_orders = ['fish', 'cococola', 'beef', 'tuna']
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich_order = sandwich_orders.pop()
#     print("I made your " + sandwich_order + " sandwich.")
#     finished_sandwiches.append(sandwich_order)

# print("I just finished those sandwich:")
# for finished_sandwiche in finished_sandwiches:
#     print(finished_sandwiche)

# # 7-9
# sandwich_orders = ['fish', 'pastrami', 'cococola',
#                    'pastrami', 'beef', 'tuna', 'pastrami']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

# 7-10
visit_places = {}
while True:
    place = raw_input(
        "If you could visit one place in the world, where would you go?\nEnter quit to leave.")
    if place == 'quit':
        break
    else:
        if place not in visit_places.keys():
            visit_places[place] = 1
        else:
            visit_places[place] += 1

print("place\tcount")
for place, count in visit_places.items():
    print(place + "\t" + str(count))
