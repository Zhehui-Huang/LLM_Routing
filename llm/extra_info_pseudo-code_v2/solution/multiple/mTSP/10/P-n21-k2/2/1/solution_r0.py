import numpy as np

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of robots (salesmen)
num_robots = 2
# Depot city
depot = 0

def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Matrix to store distances between all cities
distance_matrix = np.zeros((len(cities), len(cities)))
for i in cities:
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(i, j)