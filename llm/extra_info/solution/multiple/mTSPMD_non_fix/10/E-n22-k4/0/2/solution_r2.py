import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City and depot coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_robots = 4
depot_index = 0  # All robots start at depot city 0

# Calculate the Euclidean distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(coords[i], coords[j])
            else:
                dist_matrix[i, j] = float('inf')
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Helper function to calculate the cost of touring specific cities in order
def tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i], tour[i + 1]]
    return cost

# Assign cities to robots, starting from a single depot, optimizing using a very basic strategy
total_cities = len(coordinates)
cities_per_robot = total_cities // num_robots

# Create initial (unequal) groups of cities
groups = [
    list(range(i * cities_per_robot + 1,
               (i + 1) * cities_per_robot + 1)) for i in range(num_robots)
]
for i in range(total_cities % num_robots):
    groups[i].append(num_robots * cities_per_robot + i + 1)

# Each group starts and ends at the depot
for i in range(num_robots):
    groups[i].insert(0, depot_index)
    groups[i].append(depot_index)

# Optimize each group's path independently using permutations (This is feasible since groups are small)
optimal_paths = []
all_costs = []

for group in groups:
    best_permutation = min(
        permutations(group[1:-1]),
        key=lambda perm: tour_cost([group[0]] + list(perm) + [group[-1]], distance_matrix)
    )
    optimal_path = [group[0]] + list(best_permutation) + [group[-1]]
    optimal_paths.append(optimal_path)
    all_costs.append(tour_cost(optimal_path, distance_matrix))

# Output results
overall_cost = sum(all_costs)
for idx, path in enumerate(optimal_paths):
    print(f"Robot {idx} Tour: {path}")
    print(f"Robot {idx} Total Travel Cost: {all_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")