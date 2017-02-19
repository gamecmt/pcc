import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [x_item**3 for x_item in x]

# plt.scatter(x, y, s=10)
# plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

plt.axis([0, 5100, 0, 130000000000])
plt.show()
