import itertools
import math

# City coordinates
cities = [
    (8, 11),   # City 0 (Depot)
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

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Brute-force determination of the shortest route
best_path = None
min_cost = float("inf")

# Iterate over all possible combinations of 3 cities taken from the set of all cities except the depot
for combination in itertools.combinations(range(1, 20), 3):
    path_options = list(itertools.permutations(combination))
    
    for path in path_options:
        total_route = [0] + list(path) + [0]
        cost = sum(distance_matrix[total_route[i]][total_route[i+1]] for i in range(len(total_route) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_path = total_route

print(f"Tour: {best_path}")
print(f"Total travel cost: {min_cost}")