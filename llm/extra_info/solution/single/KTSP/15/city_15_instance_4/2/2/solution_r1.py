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

# Distance matrix computation
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Generate all permutations of 11 out of the remaining 14 cities
best_tour = None
best_cost = float('inf')

for perm in permutations([i for i in range(1, 15)], 11):  # Generate permutations of 11 cities
    tour = [0] + list(perm) + [0]  # Starting and ending at the depot city 0
    current_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    if current_cost < best_cost:
        best_tour = tour
        best_cost = current_cost

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")