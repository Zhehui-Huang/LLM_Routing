import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Initialize parameters
num_robots = 4
depots = [0, 1, 2, 3]
non_depot_cities = [i for i in cities if i not in depots]

# Helper function to calculate the Euclidean distance
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Create initial solution
def create_initial_solution():
    all_cities = non_depot_cities[:]
    random.shuffle(all_cities)
    slices = np.array_split(all_cities, num_robots)
    routes = [[depots[i]] + list(slices[i]) + [depots[i]] for i in range(num_robots)]
    return routes

# Calculate total distance of all routes
def calculate_total_distance(routes):
    total_cost = 0
    for route in routes:
        route_cost = sum(calc_distance(route[i], route[i+1]) for i in range(len(route)-1))
        total_cost += route_cost
    return total_cost

# Generating an output example:
solution = create_initial_solution()
overall_cost = calculate_total_distance(solution)

# Output the best result
print("Solution found:")
total_robot_costs = []
for idx, route in enumerate(solution):
    robot_cost = calculate_total_distance([route])
    total_robot_costs.append(robot_cost)
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {sum(total_robot_costs)}")