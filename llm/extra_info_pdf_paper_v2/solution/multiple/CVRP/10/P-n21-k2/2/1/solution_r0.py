import numpy as np
from itertools import permutations

# Data: cities coordinates and demands for each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot information
num_robots = 2
capacity = 160

# Helper Functions
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean(private_keyocity(i, j))

# Solving the CVRP using a naive approach:
# Attempt to distribute equally among robots and explore permutations for optimal routes
tours = [[] for _ in range(num_robots)]
load = [0] * num_robots
current_city = 0

def find_possible_tours(remaining_cities, tours, load):
    if not remaining_cities:
        return tours, True
    for idx, city in enumerate(remaining_cities):
        for r in range(num_robots):
            if load[r] + demands[city] <= capacity:
                new_tours = [list(tour) for tour in tours]
                new_tours[r].append(city)
                new_load = load[:]
                new_load[r] += demands[city]
                new_remaining_cities = remaining_cities[:idx] + remaining_cities[idx+1:]
                result_tours, valid = find_possible_tours(new_remaining_cities, new_tours, new_load)
                if valid:
                    return result_tours, True
    return tours, False

_, best_solution_found = find_possible_tours(list(range(1, num_cities)), tours, load)

# Form the full routes including returning to depot
full_routes = [[0] + tour + [0] for tour in best_solution_found]

# Calculate the costs
total_costs = [0] * num_robots
for i in range(num_robots):
    tour_cost = 0
    tour = full_routes[i]
    for j in range(len(tour) - 1):
        tour_cost += distance_matrix[tour[j]][tour[j + 1]]
    total_costs[i] = tour_cost

overall_total_cost = sum(total_costs)

# Output
for i in range(num_robots):
    print(f"Robot {i} Tour: {full_routes[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")