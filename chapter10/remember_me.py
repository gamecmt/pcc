import json


try:
    FileNotFoundError
except NameError:
    # py2
    FileNotFoundError = IOError


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()

    if username:
        check_username = raw_input("Are you " + username + "?(Y/N)")
        if check_username == 'Y' or check_username == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We will remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")


greet_user()
