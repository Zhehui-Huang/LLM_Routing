import math
from itertools import permutations

# Define the cities coordinates
cities = [
    (79, 15),  # City 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Precompute all distances
distance_matrix = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

def find_optimal_tour():
    n = len(cities)
    min_max_distance = float('inf')
    optimal_tour = []
    
    for perm in permutations(range(1, n)):
        # Create a round trip tour by adding the depot city at the start and the end
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_distance = 0
        
        # Evaluate the tour
        for i in range(len(tour) - 1):
            dst = distance_matrix[(tour[i], tour[i+1])]
            total_cost += dst
            max_distance = max(max_distance, dst)

        # Update the best found tour if this one has a smaller maximum distance
        if max_distance < min_max_distance:
            min_max_radius = max_distance
            optimal_tour = tour
            min_max_distance = max_distance
    
    return optimal_tour, total_cost, min_max_distance

# Finding the tour, total_cost, and max_distance
tour, total_cost, max_distance = find_optimal_tour()

# Report results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")