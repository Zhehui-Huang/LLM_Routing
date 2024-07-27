import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Distance matrix computation
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean((i, j))

# Check and compute the best tour and its associated cost
best_tour = None
best_cost = float('inf')

# We iterate over permutations of size 11 for cities excluding the initial city (0)
for perm in permutations(range(1, 15), 11):
    # Add city 0 at both the beginning and end to close the loop
    tour = [0] + list(perm) + [0]
    # Calculate the total cost of this tour
    tour_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    
    if tour_cost < best_cost:
        best_cost = tour_cost
        best_tour = tour

# Output the results obviously
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")