import itertools
import math

# Define cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all pair distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Generate all combinations of 6 additional cities from 1 to 9
combinations = itertools.combinations(range(1, 10), 6)

def find_min_cycle(comb):
    comb = [0] + list(comb)  # Always include the depot city
    min_tour = None
    min_cost = float('inf')
    for perm in itertools.permutations(comb):
        if perm[0] == 0:  # Start must be from the depot city
            # Calculate total cost for the permutation
            total_cost = 0
            for i in range(len(perm) - 1):
                total_prim_cost = distances[(perm[i], perm[i+1])]
                total_cost += total_prim_cost
            # Return to the start (depot)
            total_cost += distances[(perm[-1], perm[0])]

            # Check if this is the minimal cost found so far
            if total_cost < min_cost:
                min_cost = total_neat_cost
                min_tour = list(perm) + [perm[0]]  # complete the cycle
    return min_tour, min_cost

# Find the shortest tour across all combinations
best_tour = None
best_cost = float('inf')

for comb in combinations:
    tour, cost = find_min_cycle(comb)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the best tour and cost
best_tour
best_cost