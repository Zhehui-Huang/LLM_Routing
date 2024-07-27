import math
from itertools import permutations

# City coordinates (city_index: (x, y))
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_cost(tour):
    return sum(euclidean_point(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Helper function to compute full loop cost returning to the start
def euclidean_point(ci, cj):
    x1, y1 = cities[ci]
    x2, y2 = cities[cj]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_optimal_tour():
    # Begin with a simple initial tour, skipping the depot initially then add back
    initial_tour = list(cities.keys())[1:]  # Skip depot in the initial permutation
    best_tour = None
    best_cost = float('inf')

    # Check all permutations of cities
    for perm in permutations(initial_tour):
        # Add depot to the start and end of the tour
        full_tour = [0] + list(perm) + [0]
        cost = total_cost(full_tour)
        
        if cost < best_cost:
            best_tour = full_tour
            best_cost = cost

    return best_tour, best_cost

# Calculate optimal tour using brute force checks (feasible with small number of cities like this)
optimal_tour, optimal_cost = find_optimal_tour()

# Output format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")