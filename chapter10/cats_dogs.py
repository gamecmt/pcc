# 10-8 10-9
try:
    FileNotFoundError
except NameError:
    # py2
    FileNotFoundError = IOError


def cats_dogs(filename):
    try:
        with open(filename) as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        print("Can not found the file.")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    cats_dogs(filename)

# 10-10


def count(filename, count_name):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("Can not found the file, Please try again.")
    else:
        count = 0
        low_count = 0
        for line in lines:
            count += line.count(count_name)
            low_count += line.lower().count(count_name)
        print("There are "+str(count)+" '"+count_name+"'")
        print(low_count)

count('siddhartha.txt', 'the')
