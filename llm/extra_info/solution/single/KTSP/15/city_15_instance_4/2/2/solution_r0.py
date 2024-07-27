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
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Use permutations to determine the best tour of exactly 12 cities (including the depot)
best_tour = None
best_cost = float('inf')

for perm in permutations([i for i in range(1, 15)], 11):  # Generating permutations of 14 cities, taking 11 at a time
    tour = [0] + list(perm) + [0]  # always starting and ending at the depot
    current_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    if current_cost < best_cost:
        best_tour = tour
        best_cost = current_cost

# Display the best found tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")