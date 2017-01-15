motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('suzuki')
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motocycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 3-4
dinner = ['ak47', 'peiandsky', 'f117', 'flypig']
print('I invite ' + dinner[0] +' to have dinner.')
print('I invite ' + dinner[1] +' to have dinner.')
print('I invite ' + dinner[2] +' to have dinner.')
print('I invite ' + dinner[3] +' to have dinner.')
print('*****************************************')

# 3-5
no_dinner = dinner.pop()
print(no_dinner + " can't come.")
dinner.append('lvhua')
print('I invite ' + dinner[0] +' to have dinner.')
print('I invite ' + dinner[1] +' to have dinner.')
print('I invite ' + dinner[2] +' to have dinner.')
print('I invite ' + dinner[3] +' to have dinner.')
print('*****************************************')

# 3-6
print("I find a bigger table.")
dinner.insert(0, 'jiaji')
dinner.insert(2, 'tiger')
dinner.append('shangbin')
print('I invite ' + dinner[0] +' to have dinner.')
print('I invite ' + dinner[1] +' to have dinner.')
print('I invite ' + dinner[2] +' to have dinner.')
print('I invite ' + dinner[3] +' to have dinner.')
print('I invite ' + dinner[4] +' to have dinner.')
print('I invite ' + dinner[5] +' to have dinner.')
print('I invite ' + dinner[6] +' to have dinner.')
print('*****************************************')

# 3-7
print("The table can't timely delivery.")
print("I'm sorry "+ dinner.pop() + ", but The dinner will be postponed.")
print("I'm sorry "+ dinner.pop() + ", but The dinner will be postponed.")
print("I'm sorry "+ dinner.pop() + ", but The dinner will be postponed.")
print("I'm sorry "+ dinner.pop() + ", but The dinner will be postponed.")
print("I'm sorry "+ dinner.pop() + ", but The dinner will be postponed.")
print(dinner)
del dinner[1]
del dinner[0]
print(dinner)