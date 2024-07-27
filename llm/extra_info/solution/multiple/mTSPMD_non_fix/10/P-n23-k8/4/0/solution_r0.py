import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
import itertools

# City coordinates (depots included)
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
])

# Calculate euclidean distances between all pairs of cities
distances = cdist(coordinates, coordinates)

def solve_tsp(dist_matrix, start_node):
    """ Solves a TSP problem given a distance matrix and a starting node """
    n = len(dist_matrix)
    all_indices = set(range(n))
    path = [start_node]
    cost = 0
    
    while len(path) < n:
        last = path[-1]
        next_indices = list(all_indices - set(path))
        next_index = min(next_indices, key=lambda i: dist_matrix[last][i])
        path.append(next_index)
        cost += dist_matrix[last][next_index]
    
    return path, cost

# Define each robot starting at depot city 0
num_robots = 8
robot_initial_locations = [0] * num_robots

# Create clusters (one simple way: assign cities according to nearest depot)
assignment = np.argmin(distances[0:7, :], axis=0)  # Each city finds closest depot (including self if a depot)
clusters = {i: [] for i in range(7)}
for i, depot_index in enumerate(assignment):
    clusters[depot_index].append(i)

# Solving TSP for each cluster and calculate total costs
overall_total_cost = 0
tour_details = {}

for depot, cities in clusters.items():
    if cities:  # Ensuring there's at least one city
        tsp_path, tsp_cost = solve_tsp(distances[np.ix_(cities, cities)], cities.index(depot))
        # Translate local indices back to global indices
        full_path = [cities[idx] for idx in tsp_path]
        overall_total_cost += tsp_cost
        tour_details[depot] = {
            'tour': full_path,
            'cost': tsp_cost
        }

# Output results
for robot_id, details in tour_details.items():
    print(f"Robot {robot_id} Tour: {details['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {details['cost']}")

print(f"Overall Total Travel Cost: {overall_total_cost}")