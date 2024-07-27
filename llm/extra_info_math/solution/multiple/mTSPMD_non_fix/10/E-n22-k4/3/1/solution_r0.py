import numpy as np
from scipy.spatial import distance_matrix

# Define the city coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Calculate distance matrix (euclidean distance)
dist_matrix = distance_matrix(cities, cities)

n_cities = len(cities)
n_robots = 4
start_city = 0

def nearest_neighbor_tour(start_city, visited):
    current_city = start_city
    tour = [start_city]
    total_cost = 0
    
    while len(tour) < n_cities:
        distances = dist_matrix[current_city]
        next_city = None
        min_distance = np.inf
        
        for i in range(n_cities):
            if i not in visited and distances[i] < min_distance:
                next_city = i
                min_distance = distances[i]
        
        if next_city is None:
            break
        
        tour.append(next_city)
        visited.add(next_city)
        total_cost += min_distance
        current_city = next_city
        
    return tour, total_cost

# Running nearest neighbor for each robot
visited_cities = set([start_city])
all_tours = []
all_costs = []

for i in range(n_robots):
    tour, cost = nearest_neighbor_tour(start_city, visited_cities)
    all_tours.append(tour)
    all_costs.append(cost)

# Output the results
overall_total_cost = 0
for i in range(n_robots):
    print(f"Robot {i} Tour: {all_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {all_costs[i]}")
    overall_total_cost += all_costs[i]

print(f"Overall Total Travel Cost: {overall_total_cost}")