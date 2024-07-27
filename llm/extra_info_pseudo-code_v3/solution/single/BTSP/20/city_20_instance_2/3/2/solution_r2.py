import numpy as np
from itertools import permutations

# Coordinates of the cities including the depot city
cities = [
    (3,26), (85,72), (67,0), (50,99), (61,89), (91,56), 
    (2,65), (38,68), (3,92), (59,8), (30,88), (30,53), 
    (11,14), (52,49), (18,49), (64,41), (28,49), (91,94), 
    (51,58), (30,48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances between all pairs of cities
n = len(cities)
distances = np.array([[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)])

# Function to check if Hamiltonian circuit exists with given threshold
def is_valid_threshold(max_length):
    # Start the path from the depot city (index 0)
    remaining_cities = list(range(1, n))
    path = [0]
    max_edge_length_in_path = 0

    while remaining_cities:
        # Choose the nearest next city provided it doesn't exceed the proposed max edge length
        last_city = path[-1]
        next_city = None
        min_dist = float('inf')
        for city in remaining_cities:
            if distances[last_city][city] < min_dist and distances[last_city][city] <= max_length:
                min_dist = distances[last_city][city]
                next_city = city
        if next_city is None:
            return False, []
        path.append(next_city)
        remaining_cities.remove(next_city)
        max_edge_length_in_path = max(max_edge_length_in_path, min_dist)

    # Connect last city back to the depot, check max edge constraint
    if distances[path[-1]][0] > max_length:
        return False, []
    path.append(0)
    max_edge_length_in_path = max(max_edge_length_in_path, distances[path[-1]][0])
    return True, path

# Binary search over possible maximum edge lengths
low = 0
high = max(distances.flatten())
best_path = []
while low <= high:
    mid = (low + high) / 2
    possible, path = is_valid_threshold(mid)
    if possible:
        best_path = path
        best_max_length = mid
        high = mid - 1
    else:
        low = mid + 1

# Calculate total travel distance
total_distance = sum(distances[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))

print("Tour:", best_path)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", best_max_length)