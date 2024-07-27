import math
from itertools import combinations, permutations

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)


min_tour_cost = float('inf')
best_tour = []

# Iterate through combinations of 3 cities (not including the depot)
for combination in combinations(range(1, 15), 3):
    # Create full tours by adding the depot as starting and ending point
    full_tour_with_depot = [0] + list(combination) + [0]
    
    # Check all permutations of the 3 cities (since order matters)
    for perm in permutations(combination):
        tour_with_perm = [0] + list(perm) + [0]
        # Calculate the total travel cost for this permutation
        total_cost = sum(distance(tour_with_perm[i], tour_with_perm[i+1]) for i in range(len(tour_with_perm) - 1))
        
        # Update the minimum tour if found a shorter one
        if total_cost < min_tour_cost:
            min_tour_cost = total_cost
            best_tour = tour_with_perm

# Outputting the result
print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)