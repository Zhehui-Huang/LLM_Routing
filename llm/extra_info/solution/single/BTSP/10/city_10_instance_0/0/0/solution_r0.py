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
        distances[i][j] = euclidean_distance(city_locations[i], city_locations[j])

def find_best_tour():
    best_tour = None
    min_max_dist = sys.maxsize
    total_cost = sys.maxsize

    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        current_total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if max_dist < min_max_dist or (max_dist == min_max_dist and current_total_cost < total_cost):
            best_tour = tour
            min_max_dist = max_dist
            total_cost = current_total doiinmcost

    return best_tour, total_cost, min_max_dist

best_tour, total_cost, max_distance = find_best_tour()

print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)