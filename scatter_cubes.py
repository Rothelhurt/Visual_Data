import matplotlib.pyplot as plt

input_values = list(range(0, 5000))
cubes = [x**3 for x in input_values]

plt.scatter(input_values,cubes, c=cubes, cmap=plt.cm.Blues, s=10)

plt.title('Cube Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 6000, 0, 130000000000])

plt.show()
