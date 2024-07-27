import math
from itertools import permutations

# City coordinates indexed from 0 to 9
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Initial naive solution for simplicity: Simple permutation check
def solve_tsp_brute_force():
    cities = list(range(1, len(coordinates)))  # Excluding the depot city from permutations
    shortest_tour = None
    min_cost = float('inf')
    
    # Check all permutations of visiting order
    for p in permutations(cities):
        tour = [0] + list(p) + [0]  # Starting and ending at the depot city 0
        # Compute total travel cost
        cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Find minimum cost tour
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour
    
    return shortest_tour, min_cost

# Finding the shortest tour and total travel cost
tour, total_cost = solve_tsp_brute_force()

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")