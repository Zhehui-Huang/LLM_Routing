import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (8, 11),   # City 0 - Depot
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Calculate Euclidean distance between two cities
def distance(ci, cj):
    return math.sqrt((cities[ci][0] - cities[cj][0])**2 + (cities[ci][1] - cities[cj][1])**2)

# Initialize path from depot through all cities and back
path = list(range(len(cities))) + [0]

# Calculate the cost of an entire path
def path_cost_calc(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Perform the 2-opt algorithm to optimize the path
def two_opt(path):
    best = path
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if j - i == 1: continue
                new_path = path[:i] + path[i:j][::-1] + path[j:]
                new_cost = path_cost_calc(new_path)
                if new_cost < path_cost_calc(best):
                    best = new_path
                    improved = True
        path = best
    return best

# Optimize the given path
optimized_path = two_opt(path)

# Calculate the optimized path cost
optimized_path_cost = path_Infoath_cost_calc(optimized_path)

# Outputting the results
print("Tour:", optimized_path)
print("Total travel cost:", optimized_path_cost)