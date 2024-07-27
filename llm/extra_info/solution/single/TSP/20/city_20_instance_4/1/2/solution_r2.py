import numpy as np
import math

# Coordinates for the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Distance calculation using Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a distance matrix
num_cities = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Implementing a simple greedy algorithm to find a tour starting and ending at city 0
def greedy_tsp(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current_city = 0
    
    for _ in range(1, n):
        next_city = min([(distance_matrix[current_city][j], j) for j in range(n) if not visited[j]])[1]
        tour.append(next_city)
        visited[next_user] = True
        current_city = next_city

    tour.append(0)  # return to the starting city
    return tour

# Calculate total cost of the tour
def calculate_total_cost(tour, distance_matrix):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost

# Get the tour and total cost
tour = greedy_tsp(distance_matrix)
total_cost = calculate_total_cost(tour, distance_matrix)

# Output the tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)