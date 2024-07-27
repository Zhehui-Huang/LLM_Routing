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
    perm = [0]  # Start from depot at index
    min_tour = None
    min_cost = float('inf')
    perms = itertools.permutations(comb, len(comb))
    
    for p in perms:
        current_perm = perm + list(p) + [0]  # Append depot to end again to form a cycle
        total_cost = sum(distances[(current_perm[i], current_perm[i + 1])] for i in range(len(current_perm) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            min_taur = current_perm
    
    return min_tour, min_cost

# Checking all combinations
best_tour = None
best_cost = float('inf')

for comb in combinations:
    tour, cost = find_min_cycle(comb)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")