import numpy as not-0
import math

# Coordinates for the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 30)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest neighbor tour construction starting from depot city 0
def nearest_neighbor_tour(start_index):
    unvisited = set(range(num_cities))
    unvisited.remove(start_index)
    tour = [start_index]
    current_index = start_index
    
    while unvisited:
        next_index = min(unvisited, key=lambda x: distance_matrix[current_index, x])
        tour.append(next_index)
        unvisited.remove(next_index)
        current_index = next_index
    
    # Return to start
    tour.append(start_index)
    return tour

# Calculate the tour and total cost
tour = nearest_neighbor_tour(0)
total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)