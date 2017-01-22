# 8-1
def display_message():
    print("chapter8 function.")

display_message()

# 8-2


def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Python Crash Course")

# 8-3


def make_shirt(size, character):
    print("The shirt size is " + size + ", and the character are " + character)

make_shirt("large", "Hello")
# 8-4


def make_shirt(size, character="I love Python"):
    print("The shirt size is " + size +
          ", and the character are \"" + character + "\"")

make_shirt("large")
make_shirt("middle")
make_shirt("small", "Hello World!")
# 8-5


def describe_city(city, country="china"):
    print(city + " is in " + country)

describe_city("Reykjavik", "Iceland")
describe_city("chongqing")
describe_city("chongqing", "China")

# 8-6


def city_country(city, country):
    string = "\"" + city + "," + country + "\""
    return string

cc = city_country("Beijing", "China")
print(cc)
cc = city_country("Shanghai", "China")
print(cc)
cc = city_country("Chongqing", "China")
print(cc)


# 8-7
def make_album(artist, album):
    name = {artist: album}
    return name

cc = make_album("Beijing", "China")
print(cc)
cc = make_album("Shanghai", "China")
print(cc)
cc = make_album("Chongqing", "China")
print(cc)


# 8-8
def make_album(artist, album):
    name = {artist: album}
    return name

while True:
    user_artist = raw_input("Please enter a artist: (enter 'quit' to quit)")
    user_album = raw_input("Please enter a album: (enter 'quit' to quit)")

    if user_album == 'quit' or user_artist == 'quit':
        break
    else:
        print(make_album(user_artist, user_album))
