import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define coordinates of cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots and their starting points (depots)
depots = [0, 1, 2, 3]
n_robots = len(depots)

# Compute the Euclidean distance matrix
dist_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Assign cities to robots heuristically (simple greedy assignment based on minimal added distance to route)
assigned_cities = {robot: [depot] for robot, depot in enumerate(depots)}
remaining_cities = set(range(len(coordinates))) - set(depots)

while remaining_cities:
    min_cost = float('inf')
    chosen_city = None
    chosen_robot = None
    
    for city in remaining_cities:
        for robot, cities in assigned_cities.items():
            trial_cities = cities + [city]
            trial_tour_cost = sum(dist_matrix[trial_cities[i]][trial_cities[i+1]] for i in range(len(trial_cities)-1))
            if trial_tour_cost < min_cost:
                min_cost = trial_tour_cost
                chosen_city = city
                chosen_robot = robot
    
    assigned_cities[chosen_robot].append(chosen_city)
    remaining_cities.remove(chosen_city)

# Calculate tour for each robot using assigned cities
def calculate_min_tour(cities, depot):
    if len(cities) <= 2:
        return cities + [cities[0]], dist_matrix[cities[0]][cities[1]] * 2  # Round trip
    min_cost = float('inf')
    min_path = []
    for perm in permutations(cities[1:]): # starting from depot, permute others
        path = [depot] + list(perm) + [depot]
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost

total_cost = 0
for robot in range(n_robots):
    depot = depots[robot]
    tour, cost = calculate_min_tour(assigned_cities[robot], depot)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")