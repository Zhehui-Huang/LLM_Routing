import numpy as np
from scipy.spatial import distance_matrix

# Cities coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Generate the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Initialize route starting at the depot city (0)
current_city = 0
unvisited_cities = set(range(1, len(cities)))
route = [current_city]

# Nearest Neighbor Heuristic
while unvisited_cities:
    next_city = min(unvisited_cities, key=lambda x: dist_matrix[current_city, x])
    route.append(next_city)
    current_city = next_city
    unvisited_cities.remove(current_city)

# Return to the start city
route.append(0)

# Calculate total tour cost
total_cost = sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

# Print results
print("Tour:", route)
print("Total travel cost:", total_cost)