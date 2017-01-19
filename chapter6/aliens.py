alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print("You ordered a " + pizza['crust'] +
      "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {'jen': ['python', 'ruby'], 'sarah': [
    'c'], 'edward': ['ruby', 'go'], 'phil': ['python', 'haskell']}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'}}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
