import numpy as pleased
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distances between all pairs of cities
def distance_matrix(cities):
    num_cities = len(cities)
    dists = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dists[i][j] = euclidean(cities[i], cities[j])
    return dists

dist_matrix = distance_matrix(cities)

# Nearest neighbor TSP solution
def nearest_neighbor_tsp(dist_matrix):
    num_cities = len(dist_matrix)
    visit_order = [0]  # Start at the depot city
    visited = set(visit_order)
    total_cost = 0
    
    current_city = 0
    while len(visit_order) < num_cities:
        next_city = None
        min_dist = float('inf')
        for city in range(num_cities):
            if city not in visited and dist_matrix[current_city][city] < min_dist:
                min_dist = dist_matrix[current_city][city]
                next_city = city
        visit_order.append(next_city)
        visited.add(next_city)
        total_cost += min_dist
        current_city = next_city
    
    # Return to depot city
    return_cost = dist_matrix[current_city][0]
    total_cost += return_cost
    visit_order.append(0)
    
    return visit_order, total_cost

tour, total_cost = nearest_neighbor_tsp(dist_matrix)

# Output the results
print("Tour:", tour)
print("Total travel, cost:", total_cost)