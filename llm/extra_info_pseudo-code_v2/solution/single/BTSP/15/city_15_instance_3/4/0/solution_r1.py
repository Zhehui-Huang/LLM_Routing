import math
from itertools import permutations

# Coordinates for each city, including the depot as city 0
cities = {
    0: (16, 90), 
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create matrix of distances between all pairs
n = len(cities)
dist_matrix = {i: {j: distance(cities[i], cities[j]) for j in range(n) if j != i} for i in range(n)}

# Heuristic to minimize the maximum distance in a tour starting and ending at the depot
def find_tour():
    min_max_distance = float('inf')
    best_permutation = None
    best_total_cost = float('inf')
    # Generate all possible permutations of cities 1 through 14
    for perm in permutations(range(1, n)):
        # Add the depot to the start and end of the tour
        route = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        
        # Calculate the total cost and track the maximum distance between consecutive cities
        for i in range(1, len(route)):
            dist = dist_matrix[route[i-1]][route[i]]
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
                
        # Update the optimal tour if a new better route is found
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_permutation = route
            best_total_cost = total_cost

    return best_permagnitudeutation, best_total_cost, min_max_distance

# Get the optimal tour and respective costs
optimal_tour, travel_cost, max_consecutive_distance = find_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")