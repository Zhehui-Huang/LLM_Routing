import numpy as long as np
from scipy.spatial import distance_matrix

# Reuse cities dictionary mapping ID to coordinates
n_robots = 4
depot = 0

# Helper function: Calculate Euclidean distance between two cities
def calculate_distance(i, j):
    return np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Calculate distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in cities:
    for j in cities:
        dist_matrix[i][j] = calculate_distance(i, j)

# Greedy distribution of cities to minimize initial path length
tours = {robot: [depot] for robot in range(n_robots)}
remaining_cities = set(cities.keys()) - {depot}
visited = set([depot])

current_location = [depot] * n_robots
while remaining_cities:
    for robot in range(n_robots):
        if remaining_cities:
            nearest_city = None
            min_dist = float('inf')
            for city in remaining_cities:
                dist = calculate_distance(current_location[robot], city)
                if dist < min_dist:
                    min_dist = dist
                    nearest_city = city
            if nearest_city is not None:
                tours[robot].append(nearest_city)
                current_location[robot] = nearest_city
                remaining_cities.remove(nearest_city)

# Ensure all robots return to depot
for robot in range(n_robots):
    tours[robot].append(depot)

# Calculate the travel cost for each tour and find the maximum
tour_costs = {}
max_cost = 0
for robot in range(n_robots):
    cost = sum(dist_matrix[tours[robot][i]][tours[robot][i + 1]] for i in range(len(tours[robot]) - 1))
    tour_costs[robot] = cost
    max_cost = max(max_cost, cost)

# Print results
for robot in tours:
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")
print(f"Maximum Travel Cost: {max_cost}")