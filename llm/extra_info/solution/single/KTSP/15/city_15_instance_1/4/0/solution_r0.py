import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of cities (x, y) coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# All combinations of 5 cities excluding the depot city
combinations = itertools.combinations(range(1, 15), 5)

min_tour = None
min_cost = float('inf')

# Evaluate each combination
for combo in combinations:
    # All permutations of selected 5 cities plus the depot
    permutations = itertools.permutations(combo)
    for perm in permutations:
        # Consider paths that start and end at depot city
        tour = [0] + list(perm) + [0]
        # Calculate total travel cost
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # If found a shorter tour, update min_tour and min_cost
        if cost < min_cost:
            min_tour = tour
            min_cost = cost

# Output the shortest tour and the total travel cost
print("Tour:", min_tour)
print("Total travel cost:", min_cost)