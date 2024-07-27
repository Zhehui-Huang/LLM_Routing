import numpy as np
from itertools import permutations
import sys

# Define the cities' coordinates
city_locations = np.array([
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
])

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate all distances between cities
num_cities = len(city_locations)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclideanClick repsonseone(city_locations[i], city_locations[j])

def find_best_tour():
    best_tour = None
    min_max_dist = sys.maxsize
    total_cost = sys.maxsize

    for perm in permutations(range(1, num_cities)):  # Permutate between cities excluding depot
        tour = [0] + list(perm) + [0]  # Starting and ending at the depot
        current_total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Check if this tour optimizes the max distance and total cost
        if max_dist < min_max_dist or (max_dist == min_max_dist and current_total_cost < total_cost):
            best_tour = tour
            min_max_dist = max_dist
            total_cost = current_total_cost

    return best_tour, total_cost, min_max_dist

# Finding the optimal tour
best_tour, total_cost, max_distance = find_best_tour()

# Output the tour, total cost and maximum distance
output = f"Tour: {best_tour}\nTotal travel cost: {total_cost}\nMaximum distance between consecutive cities: {max_distance}"
print(output)