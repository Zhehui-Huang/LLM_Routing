import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_minimal_tour(cities):
    """Compute the tour minimizing the maximum distance between consecutive cities."""
    n = len(cities)
    
    # Distance matrix
    distances = [
        [euclidean_distance(cities[i], cities[j]) for j in range(n)]
        for i in range(n)
    ]

    # Start from the depot city 0
    best_max_leg = float('inf')
    best_tour = None
    best_total_cost = float('inf')

    # Use permutations to find best tour since n=10 is small
    for perm in permutations(range(1, n)):  # Start from 1 to omit depot city in permutations
        tour = [0] + list(perm) + [0]
        max_leg = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_leg < best_max_leg or (max_leg == best_max_leg and total_cost < best_total_cost):
            best_max_leg = max_leg
            best_tour = tour
            best_total_cost = total_cost
            
    return best_tour, best_total_cost, best_max_tour

# Define the coordinates of each city
cities = [
    (90, 3),   # Depot
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Calculate the best tour minimizing the longest single travel 
tour, total_cost, max_distance = find_minimal_tour(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")