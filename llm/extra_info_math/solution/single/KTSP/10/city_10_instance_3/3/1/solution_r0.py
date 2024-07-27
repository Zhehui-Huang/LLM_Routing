import math
from itertools import permutations

# City coordinates
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)   # City 9
]

# Number of cities
n = 10

# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of cities to visit including depot
k = 7

# Generate all subsets of size k that start and end at the depot city (index 0)
def valid_subsets(size, include):
    subsets = []
    for comb in permutations(range(1, n), size-1):
        subset = [include] + list(comb)
        if len(set(subset)) == size:
            subsets.append(subset)
    return subsets

# All possible subsets of cities including the depot
city_subsets = valid_subsets(k, 0)

# Function to compute total distance of a path
def path_distance(path):
    return sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))

# Heuristic for finding a reasonable path within a subset
def find_best_tour(subsets):
    min_distance = float('inf')
    best_tour = None
    
    for subset in subsets:
        for perm in permutations(subset[1:]):
            current_tour = [subset[0]] + list(perm) + [subset[0]]
            current_distance = path_distance(current_tour)
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = current_tour
    return best_tour, min_distance

# Finding the shortest cycle
best_cycle, min_cycle_distance = find_best_tour(city_subsets)

# Output
print("Tour:", best_cycle)
print("Total travel cost:", min_cycle_distance)