import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = list(range(1,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('d6*d6.svg')
