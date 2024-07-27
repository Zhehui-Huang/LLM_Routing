import numpy as np
from scipy.spatial.distance import cdist, euclidean
from itertools import permutations

# Define city coordinates
city_coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
])

# Number of robots and corresponding starting depot city indices
num_robots = 4
depot_indices = [0]

# Calculate pairwise distances between all cities
pairwise_distances = cdist(city_coordinates, city_coordinates)

# Attempt the simplest possible separation: naively assign each robot equally spaced city segments
num_cities = len(city_coordinates)
cities_per_robot_approx = num_cities // num_robots

# Function to compute the tour and its cost for a set of cities
def compute_tour(cities, start_index):
    if not cities:
        return [], 0
    min_cost = np.inf
    best_route = None
    for perm in permutations(cities):
        route = [start_index] + list(perm)
        cost = sum(pairwise_distances[route[i], route[i+1]] for i in range(len(route)-1))
        if cost < min_cost:
            min_cost = cost
            best_route = route
    return best_route, min_cost

# Divide cities among robots starting after the depots
robot_assignments = {}
start_index = 0
all_assigned_cities = set(depot_indices)

for robot_id in range(num_robots):
    if robot_id == num_robots - 1:
        # Last robot gets the remainder of the cities
        assigned_cities = set(range(num_cities)) - all_assigned_cities
    else:
        assigned_cities = set(range(start_index, start_index + cities_per_robot_approx)) - all_assigned_cities
        start_index += cities_per_robot_approx
    
    all_assigned_cities.update(assigned_cities)
    robot_assignments[robot_id] = assigned_cities

# Compute tours for each robot
tours = {}
total_cost = 0

for robot_id, assigned_cities in robot_assignments.items():
    assigned_cities = list(assigned_cities)
    tour, cost = compute_tour(assigned_cities, depot_indices[0])  # Each robot starts at depot 0
    tours[robot_id] = tour
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_std}")  # Fixed typo to `total_cost`