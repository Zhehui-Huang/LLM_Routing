import math
import itertools

# Coordinate positions for the cities
city_positions = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distances between each pair of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Matrix of distances
distances = {}
for i in city_positions:
    for j in city_positions:
        if i != j:
            distances[(i, j)] = euclidean_distance(city_positions[i], city_positions[j])