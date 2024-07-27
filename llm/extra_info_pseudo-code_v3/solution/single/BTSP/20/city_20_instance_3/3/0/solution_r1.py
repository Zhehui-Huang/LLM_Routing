import numpy as np
from scipy.spatial.distance import euclidean

# Provided city coordinates with index representing the respective city
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

num_cities = len(city_coords)
distance_matrix = np.zeros((num_cities, num_cities))

# Fill distance matrix
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(city_coords[i], city_coords[j])
        else:
            distance_matrix[i][j] = float('inf')  # No self-loops

def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_data_city
    
    tour.append(start_city)  # return to the start city
    return tour

# Calculate tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(0)

# Calculate maximum distance and total cost
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distance_matrix[tour[i]][tour[i + 1]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")