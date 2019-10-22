import pygal

from die import Die

# Создание 2-х D6 кубиков.
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков и сохранения результатов в списке.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация данных.
hist = pygal.Bar()
hist.title = 'Results of rolling D6 and D10 50000 times.'
hist.x_title = 'Result'
hist.x_labels = [str(val) for val in range(2, max_result+1)]
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')