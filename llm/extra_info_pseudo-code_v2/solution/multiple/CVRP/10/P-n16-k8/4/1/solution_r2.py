import numpy as np
from scipy.spatial.distance import euclidean
from heapq import heappush, heappop

# Constants
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}
robot_capacity = 35
num_robots = 8

# Helper functions
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Calculate all-to-all distances
dist_matrix = np.zeros((len(cities), len(cities)))
for i in cities:
    for j in cities:
        dist_matrix[i][j] = distance(i, j)

# Clarke-Wright Savings Calculation
savings = []
for i in range(1, len(cities)):
    for j in range(i + 1, len(cities)):
        s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
        savings.append((s, i, j))
savings = sorted(savings, reverse=True, key=lambda x: x[0])  # Sort by saving descending

# Setup robots (route including depot return, load, and travel cost)
robots = [{'route': [0], 'load': 0, 'travel_cost': 0} for _ in range(num_robots)]

# Function to assign cities to robots based on CW savings
def assign_cities_to_robots():
    unassigned_cities = set(cities.keys()) - {0}  # Exclude depot
    while unassigned_cities:
        for saving, city1, city2 in savings:
            if city1 in unassigned_cities and city2 in unassigned_cities:
                # Try to add both cities to the same robot if possible
                for robot in robots:
                    if robot['load'] + demands[city1] + demands[city2] <= robot_capacity:
                        updated_route = robot['route'][:-1] + [city1, city2, 0]
                        # Calculate the marginal cost of adding these two cities
                        cost_if_added = robot['travel_cost'] - dist_matrix[robot['route'][-2]][0] \
                                        + dist_matrix[robot['route'][-2]][city1] + dist_matrix[city1][city2] + dist_instance[city2][0]
                        if cost_if_added - robot['travel_cost'] < saving:
                            robot['route'] = updated_route
                            robot['travel_cost'] = cost_if_added
                            robot['load'] += demands[city1] + demands[city2]
                            unassigned_cities.remove(city1)
                            unassigned_cities.remove(city2)
                            break

# Perform the assignment
assign_cities_to_robots()

# Output results
total_cost = 0
for idx, robot in enumerate(robots):
    print(f"Robot {idx} Tour: {robot['route']}")
    print(f"Robot {idx} Total Travel Cost: {robot['travel_cost']}")
    total_cost += robot['travel_cost']

print(f"Overall Total Travel Cost: {total_cost}")