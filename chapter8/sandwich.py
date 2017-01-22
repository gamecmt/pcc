# 8-12
def sandwich(*topping):
    print(topping)

sandwich('a')
sandwich('b', 'c', 'd')
sandwich('e', 'f', 'g')

# 8-13


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    'mt', 'c', location='chongqing', field='IT')
print(user_profile)

# 8-14


def make_car(manufacturer, model, **car_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    print(profile)

car = make_car('sabaru', 'outback', color='blue', tow_package=True)
