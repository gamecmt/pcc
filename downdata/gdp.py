import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code

filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdp = {}

for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2014':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for code,gdp in cc_gdp.items():
    if gdp<10000000000:
        cc_gdp_1[code]=gdp
    elif gdp<1000000000000:
        cc_gdp_2[code]=gdp
    else:
        cc_gdp_3[code]=gdp

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2014, by Country'
wm.add('gdp<1e10', cc_gdp_1)
wm.add('1e10<gdp<1e12', cc_gdp_2)
wm.add('1e12<gdp', cc_gdp_3)

wm.render_to_file('gdp.svg')
