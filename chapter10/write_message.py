filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10-3
name = raw_input("Enter your name: ")
with open('name.txt', 'w') as file_object:
    file_object.write(name)

# 10-4
while True:
    name = raw_input("Enter your name: ")
    if name == 'quit':
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(name + "\n")

# 10-5
thatiswhy = 'thatiswhy.txt'

while True:
    why = raw_input("Why are you like programming?(enter 'quit' to quit)")
    if why == 'quit':
        break
    else:
        with open(thatiswhy, 'a') as file_object:
            file_object.write(name + "\n")
