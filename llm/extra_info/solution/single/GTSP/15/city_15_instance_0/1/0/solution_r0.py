import itertools
import math

# City coordinates with depot city included
coordinates = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Groups of cities
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Euclidean distance function
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix computation
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Find the shortest route that visits one city from each group
def find_shortest_route():
    min_distance = float('inf')
    best_tour = None
    
    # Iterating over all combinations of choosing exactly one city from each group
    for cities in itertools.product(*groups):
        # Including the depot
        full_route = [0] + list(cities) + [0]
        
        # Check all permutations of the selected cities
        for perm in itertools.permutations(cities):
            current_route = [0] + list(perm) + [0]
            current_distance = sum(distance_matrix[current_route[i]][current_route[i+1]] for i in range(len(current_route) - 1))
            
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = current_route
                
    return best_tour, min_distance

# Compute the best tour and its cost
tour, total_cost = find_shortest_route()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")