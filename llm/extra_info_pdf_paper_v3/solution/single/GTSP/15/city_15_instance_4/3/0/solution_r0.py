import numpy as np
from itertools import permutations
from math import sqrt

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1_idx, city2_idx):
    x1, y1 = coordinates[city1_idx]
    x2, y2 = coordinates[city2_idx]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(i, j)

# Find the minimum tour
def find_minimum_tour():
    min_tour_cost = float('inf')
    best_tour = None
    
    # Iterate over all permutations of one city from each group
    for combination in permutations([g[0] for g in groups]):
        # Calculate the tour cost based on sequence starting from depot (0)
        # visiting selected cities and then returning to depot
        tour = [0] + list(combination) + [0]
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i+1]]

        # Update if the current permutation has a smaller cost than previously found
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = tour
            
    return best_tour, min_tour_cost

# Find the best tour
tour, cost = find_minimum_tour()

print("Tour:", tour)
print("Total travel cost:", round(cost, 2))