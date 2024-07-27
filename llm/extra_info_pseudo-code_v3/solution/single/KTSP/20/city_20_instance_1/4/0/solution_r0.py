import numpy as np
from itertools import permutations

# Given city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 
    14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45), 
    18: (50, 28), 19: (69, 9)
}

# Distance function between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of n-k cities to include in the tour, where n is total cities and k is tour size
def generate_initial_solutions(base, n, k):
    from itertools import combinations
    base_set = set(base)
    other_cities = list(set(range(n)) - base_set)
    for comb in combinations(other_cities, k - len(base)):
        yield list(base) + list(comb)

# Calculate the cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Heuristic to find the shortest tour among permutations of a given set of cities
def find_shortest_tour(cities):
    shortest_tour = None
    min_cost = float('inf')
    for perm in permutations(cities):
        perm = list(perm)
        perm.append(perm[0])  # Return to the start city
        cost = tour_cost(perm)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = perm
    return shortest_tour, min_cost

# Main variable to use for selecting the best initial tour
best_tour, best_cost = None, float('inf')

# Choose the base to always include the depot (city 0)
base = [0]

# Iterate over initial solutions and find the globally shortest tour
for tour in generate_initial_actions(base, len(cities), 7):  # We need 7 cities including the depot
    current_tour, current_cost = find_shortest_tour(tour)
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_tour

# Output result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")