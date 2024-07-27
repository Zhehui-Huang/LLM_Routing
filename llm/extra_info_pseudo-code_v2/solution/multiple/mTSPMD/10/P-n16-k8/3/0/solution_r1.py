import numpy as np
from scipy.spatial.distance import euclidean

# Data initialization
depots = list(range(8))
cities = list(range(8, 16))
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Initialize distances
distances = {(i, j): euclidean(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j}

# Tour construction for each robot
tours = {depot: [depot] for depot in depots}
overall_cost = 0

# Simple heuristic for assignment (greedy nearest neighbour)
for city in cities:
    closest_depot = min(depots, key=lambda d: distances[(d, city)] + distances[(city, d)])
    tours[closest_depot].append(city)

# Complete the tours, returning to depots
for depot, tour in tours.items():
    tour.append(depot)

# Calculate travel cost for each robot
for depot, tour in tours.items():
    tour_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")