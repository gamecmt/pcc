my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 4-10
print("The first three items in the list are:")
for i in my_foods[:3]:
	print(i.title())

print("Three items from the middle of the list are:")
for i in my_foods[1:4]:
	print(i)

print("The last three items in the list are:")
for i in my_foods[-3:]:
	print(i)

# 4-11
my_pizzas = ['a', 'b', 'c', 'd', 'e']
friend_pizzas = my_pizzas[:]

my_pizzas.append('f')
friend_pizzas.append('g')

print("My favorite pizzas are:")
for i in my_pizzas:
	print(i.title())

print("My friend's favorite pizzas are:")
for i in friend_pizzas:
	print(i)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for i in my_foods:
	print(i)
for i in friend_foods:
	print(i)