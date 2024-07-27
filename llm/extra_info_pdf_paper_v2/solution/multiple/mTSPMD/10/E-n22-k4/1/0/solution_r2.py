import numpy as np
import math

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4
depots = {i: i for i in range(num_robots)}

# Build distance matrix
dist_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Greedy assignment of cities to robots (round-robin distribution to balance the assignment)
tours = {robot: [depot] for robot, depot in depots.items()}
assigned_cities = set(depots.values())

city_indices = list(range(len(cities)))
np.random.shuffle(city_indices)  # Randomize city visit order

for city in city_indices:
    if city not in assigned_cities:
        # Assign city to robot with the least travel cost increase
        min_cost = float('inf')
        best_robot = None
        for robot, tour in tours.items():
            last_city = tour[-1]
            cost = dist_matrix[last_city][city]
            if cost < min_cost:
                min_cost = cost
                best_robot = robot
        tours[best_robot].append(city)
        assigned_cities.add(city)

# Have each robot return to its start depot
for robot, tour in tours.items():
    tour.append(depots[robot])

# Calculate tour costs and total cost
total_cost = 0
tour_costs = {}
for robot, tour in tours.items():
    cost = 0
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1]][tour[i]]
    tour_costs[robot] = cost
    total_cost += cost

# Display the results
for robot in tours:
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")