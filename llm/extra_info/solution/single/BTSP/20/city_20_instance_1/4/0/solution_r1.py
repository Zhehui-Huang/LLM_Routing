import math
import numpy as np

# Define the coordinates of each city, including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities
num_cities = len(coordinates)

# Create a distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = distance(i, j)

# Function to evaluate a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = dist_matrix[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Greedy algorithm to minimize the maximum segment length
def greedy_minmax_tour():
    unvisited = set(range(1, num_cities))
    tour = [0]  # Start at the depot
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # Return to depot
    return tour

# Construct a greedy tour
tour = greedy_minmax_tour()

# Evaluate the tour
total_cost, max_distance = evaluate_tour(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")