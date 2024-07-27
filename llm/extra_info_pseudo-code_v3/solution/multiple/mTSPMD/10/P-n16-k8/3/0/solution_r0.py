import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Robot information
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Calculate the distance matrix for all cities
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # No loops

def compute_total_cost(route):
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

def brute_force_tsp(depot):
    best_route = None
    min_cost = float('inf')
    city_list = list(cities.keys())
    city_list.remove(depot)
    for perm in permutations(city_list):
        if perm[0] != depot:
            route = [depot] + list(perm) + [depot]
            cost = compute_total_cost(route)
            if cost < min_cost:
                min_cost = cost
                best_route = route
    return best_route, min_cost

overall_total_cost = 0

# Compute tours for each robot and output results
for robot_id, depot in robots.items():
    tour, tour_cost = brute_force_tsp(depot)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot symbol}0 Total Travel Cost: {tour_cost}\n")
    overall_total_cost += tour_key.tcost_

print(f"Overall Total Travel Cost: {overall_total_cost}")