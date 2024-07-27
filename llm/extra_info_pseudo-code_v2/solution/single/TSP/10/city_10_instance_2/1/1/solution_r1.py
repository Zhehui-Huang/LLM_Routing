import math
import numpy as np

# Given coordinates of the cities
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a distance matrix
def create_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Nearest neighbor algorithm for generating an initial tour
def nearest_neighbour_tour(start, distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = list(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_body)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # Returning to the depot
    return tour

# Calculate the total travel cost of a given tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

# Convert coordinates dictionary to a list
coord_list = [coordinates[i] for i in range(len(coordinates))]

# Generate the distance matrix for all cities
distance_matrix = create_distance_matrix(coord_list)

# Generate an initial tour using the nearest neighbor algorithm
initial_tour = nearest_neighbour_tour(0, distance_matrix)

# Calculate the cost of the initial tour 
initial_cost = calculate_tour_cost(initial_tour, distance_matrix)

# Ideally, we'd apply a Lin-Kernighan heuristic here to improve the tour
# Lacking the full implementation, we will use the initial tour for demonstration

print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)