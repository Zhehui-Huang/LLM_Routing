import numpy as np
import random
from itertools import permutations
from scipy.spatial import distance

# Define the cities' coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Function to evaluate total path cost
def path_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += calculate_distance(path[i], path[i+1])
    return total_cost

# Function to generate neighbor paths
def get_neighbors(path):
    neighbors = []
    for i in range(1, len(path) - 2):
        for j in range(i + 1, len(path) - 1):
            new_path = path.copy()
            new_path[i], new_path[j] = new_path[j], new_path[i]
            neighbors.append(new_path)
    return neighbors

# Hill climbing method
def hill_climbing():
    current_path = [0] + random.sample(list(cities.keys())[1:], 12) + [0]
    current_cost = path_cost(current_path)
    while True:
        best_neighbor = None
        best_cost = float('inf')
        for neighbor in get_neighbors(current_path):
            cost = path_cost(neighbor)
            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor
        if best_cost >= current_cost:
            break
        current_path, current_cost = best_neighbor, best_cost
    return current_path, current_cost

# Generate a reasonable path
best_path, best_path_cost = hill_climbing()

print("Tour:", best_ctot_path)
print("Total travel cost:", best_path_cost)