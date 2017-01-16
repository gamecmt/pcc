for value in range(1,5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value**2 for value in range(1, 11)]
print(squares)

# 4-3
twenty = list(range(1, 21))
print(twenty)

# 4-4
millions = list(range(1, 1000001))
# for million in millions:
# 	print million

# 4-5
print(min(millions))
print(max(millions))
print(sum(millions))

# 4-6
odds = list(range(1, 20, 2))
for odd in odds:
	print(odd)

# 4-7
threes = list(range(3, 31, 3))
for three in threes:
	print(three)

# 4-8
lists = []
for value in range(1,11):
	list = value**3
	lists.append(list)

for list in lists:
	print(list)

# 4-9
clubs = [value**3 for value in range(1,11)]
for club in clubs:
	print club