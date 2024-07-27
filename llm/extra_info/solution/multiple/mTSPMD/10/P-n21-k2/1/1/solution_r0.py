import math
import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_distance_matrix(cities):
    coords = np.array(cities)
    return distance_matrix(coords, coords)

def find_minimum_tour(cities, depot_index, dist_matrix):
    # we consider all cities except the depot city itself for permutations
    min_tour = None
    min_cost = float('inf')
    
    for perm in permutations(cities):
        cost = dist_matrix[depot_index][perm[0]]  # start from depot to first city
        for i in range(len(perm) - 1):
            cost += dist_matrix[perm[i]][perm[i + 1]]
        cost += dist_matrix[perm[-1]][depot_index]  # return to the depot
        
        if cost < min_cost:
            min_tour = perm
            min_cost = cost
    
    # Include depot at both start and the end of the tour
    return [depot_index] + list(min_tour) + [depot_index], min_cost

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]  # Depots indices
non_depots = list(set(range(len(cites))) - set(depots))
# Calculate distance matrix
dist_matrix = create_distance_matrix(cities)

# Assign cities to clusters based on the nearest depot by heuristic
clusters = {depot: [] for depot in depots}
for city in non_depots:
    nearest_depot = min(depots, key=lambda d: dist_matrix[d][city])
    clusters[nearest_depot].append(city)

# Find tours and their costs for each robot
total_travel_cost = 0
for depot, depot_cities in clusters.items():
    tour, cost = find_minimum_tour(depot_cities, depot, dist_matrix)
    total_travel_cost += cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")