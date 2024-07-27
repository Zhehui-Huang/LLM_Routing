import numpy as np
import networkx as nx
from itertools import permutations

# City coordinates, including the depot city
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities and calculation of distance matrix
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = calculate_distance(coordinates[i], coordinates[j])

# Finding a tour with the smallest maximum distance between consecutive cities
def find_bottleneck_tour():
    max_distance_thresholds = np.unique(distances)
    max_distance_thresholds.sort()
    
    for threshold in max_distance_thresholds:
        # Create graph where edges only exist if under the threshold distance
        G = nx.Graph()
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                if distances[i, j] <= threshold:
                    G.add_edge(i, j)

        # Check for Hamiltonian cycle
        if nx.is_connected(G) and G.number_of_nodes() == num_cities:
            for path in permutations(range(1, num_cities)):
                full_path = [0] + list(path) + [0]
                valid = True
                for k in range(len(full_path) - 1):
                    if distances[full_path[k], full_path[k+1]] > threshold:
                        valid = False
                        break
                if valid:
                    total_distance = sum(distances[full_path[i], full_path[i+1]] for i in range(len(full_path) - 1))
                    max_distance = max(distances[full_path[i], full_path[i+1]] for i in range(len(full_path) - 1))
                    return full_path, total_distance, max_distance

    return [], 0, 0  # If no tour satisfies the criterion, return empty tour

# Compute the satisfactory tour
tour, total_travel_cost, max_consecutive_distance = find_bottleneck_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)