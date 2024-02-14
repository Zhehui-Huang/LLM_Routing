import matplotlib.pyplot as plt

# Coordinates of the places
places = {'Place 1': (9, 4), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 2': (4, 6), 'Place 5': (4, 8)}

# Plot the positions of the places
for place, (x, y) in places.items():
    plt.plot(x, y, 'o', label=place)

# Solution path
path = ['Place 1', 'Place 3', 'Place 4', 'Place 2', 'Place 5', 'Place 1']

# Draw arrows for the path
for i in range(len(path) - 1):
    start = places[path[i]]
    end = places[path[i + 1]]
    plt.annotate("", xy=end, xycoords='data', xytext=start, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.legend()
plt.grid(True)
plt.title("Solution Visualization")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.show()