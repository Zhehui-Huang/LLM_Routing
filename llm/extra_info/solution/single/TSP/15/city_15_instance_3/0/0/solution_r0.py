import numpy as np

# Define the cities' coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Nearest neighbor heuristic to find an initial solution for the TSP
def nearest_neighbor_tour(start, distance_matrix):
    n = len(distance_matrix)
    unvisited = list(range(n))
    tour = [start]
    unvisited.remove(start)
    
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to the starting city
    return tour

# Calculate the total distance of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total
    return total_cost

# Generate a tour using nearest neighbor starting from depot city (index 0)
tour = nearest_neighbor_tour(0, distance_matrix)
total_cost = calculate_tour_cost(tour, distance_matrix)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)