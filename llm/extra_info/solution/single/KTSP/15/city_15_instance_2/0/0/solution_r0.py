from itertools import combinations, permutations
from math import sqrt

# Coordinates of the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of 7 cities from the given 14 non-depot cities
combs = combinations([i for i in range(1, 15)], 7)

best_tour = None
minimal_cost = float('inf')

# Iterate over all combinations of cities
for comb in combs:
    full_route = [0] + list(comb) + [0]
    
    # Permute through all possible orders of visiting the selected cities
    for perm in permutations(comb):
        route = [0] + list(perm) + [0]
        # Calculate the total travel cost for this route
        cost = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
        
        # Check if this route is the shortest one found so far
        if cost < minimal_cost:
            minimal_cost = cost
            best_tour = route

print("Tour:", best_tour)
print("Total travel cost:", minimal_cost)