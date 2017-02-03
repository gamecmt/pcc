import json

try:
    FileNotFoundError
except NameError:
    # py2
    FileNotFoundError = IOError


def get_new_favorite_number():
    number = raw_input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number


def get_stored_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def greet_number():
    number = get_stored_favorite_number()
    if number:
        print("I know your favorite number! It's " + number)
    else:
        number = get_new_favorite_number()
        print("We will remember your favorite number next.")

greet_number()
