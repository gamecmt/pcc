# 11-1
def city_country(city, country, population=''):
    if population:
        return city.title() + ", " + country.title() + " - population " + population
    else:
        return city.title() + ", " + country.title()
