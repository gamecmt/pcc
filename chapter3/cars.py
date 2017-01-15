cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# cars.sort(reverse=True)
# print(cars)

print("Here is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\nHere is the original list again: ")
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print len(cars)

# 3-8
# sorted 不能使用reverse=True 而 sort可以
