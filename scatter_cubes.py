import matplotlib.pyplot as plt

x_values = range(1, 500)
y_values = [value**3 for value in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 550, 0, 130000000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()


