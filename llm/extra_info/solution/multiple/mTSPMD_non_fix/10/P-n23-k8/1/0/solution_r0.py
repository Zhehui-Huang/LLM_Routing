import numpy as np
import math

# City coordinates with indices corresponding to city numbers
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Distance calculation function
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Matrix to store distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

# Populate distance matrix
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = calculate_distance(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')

# Nearest neighbor heuristic
def nearest_neighbor_tour(start_city, unused_cities, distances):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unused_cities:
        next_city = min(unused_cities, key=lambda city: distances[current_city, city])
        total_cost += distances[current_city, next_city]
        current_city = next_city
        tour.append(current_city)
        unused_cities.remove(current_city)
    
    return tour, total_cost

# Assign cities to robots
unused_cities = set(range(1, num_cities))
tours = []
costs = []

# Distribute cities to robots
for i in range(num_robots):
    if not unused_cities:
        break
    tour, cost = nearest_neighbor_tour(0, unused_cities, distances)
    tours.append(tour)
    costs.append(cost)

# Display tours and costs
overall_cost = 0
for i, tour in enumerate(tours):
    if len(tour) > 1:
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
        overall_cost += costs[i]

print(f"Overall Total Travel Cost: {overall_cost}")