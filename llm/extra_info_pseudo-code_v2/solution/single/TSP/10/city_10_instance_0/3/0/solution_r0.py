import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def solve_tsp(coordinates):
    # Initial set up
    cities = coordinates
    n = len(cities)
    min_tour = None
    min_cost = float('inf')

    # Generate all permutations of city indices to find the minimum tour
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0] # tour starting and ending at depot city 0
        cost = total_cost(tour, cities)
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    
    return min_tour, min_cost

# Define city positions
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Compute the solution
tour, cost = solve_tsp(cities)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", cost)