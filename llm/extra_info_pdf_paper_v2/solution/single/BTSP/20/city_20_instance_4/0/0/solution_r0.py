import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create the graph
edges = []
num_cities = len(cities)

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        edges.append((i, j, euclidean_dist(i, j)))

# Sort edges by distance
edges = sorted(edges, key=lambda x: x[2])