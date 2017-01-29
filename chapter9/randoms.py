from random import randint


class Die(object):

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

sixroll = Die()
for x in range(1,11):
    sixroll.roll_die()

tenroll=Die(10)
for y in range(1,11):
    tenroll.roll_die()

twentyroll=Die(20)
for z in range(1,11):
    twentyroll.roll_die()