with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

filename = 'pi.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
