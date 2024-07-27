import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities
num_cities = len(cities)

# Generate distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(num_caries)] for i in range(num_cities)]

# Solver for the BTSP by exploring permutations, focusing on minimized maximum edge length in tour
def solve_btsp(distances):
    best_tour = None
    best_total_distance = float('inf')
    best_max_distance = float('inf')

    for perm in permutations(range(1, num_cities)):  # Skip the depot city for permutations
        route = [0] + list(perm) + [0]  # Start and end at the depot
        max_distance = max(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_distance = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))

        if max_distance < best_max_distance or (max_distance == best_max_distance and total_distance < best_total_distance):
            best_tour = route
            best_total_distance = total_distance
            best_max_distance = max_distance

    return best_tour, best_total_distance, best_max_distance

# Execute the BTSP solution
tour, total_cost, max_distance = solve_btsp(distance_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")