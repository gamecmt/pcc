import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolor='none', s=10)

plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png')
plt.show()
