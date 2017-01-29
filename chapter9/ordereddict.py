# 9-13

from collections import OrderedDict

program_dicts = OrderedDict()

program_dicts['boolean'] = "a boolean"
program_dicts['rgbcolor'] = "a color"
program_dicts['type'] = "An osa type value with the given 4-character name"

for name, explan in program_dicts.items():
    print(name.title() + ": " + explan.title())
