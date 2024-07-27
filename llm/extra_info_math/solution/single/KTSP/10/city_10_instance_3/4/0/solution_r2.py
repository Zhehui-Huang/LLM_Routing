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

# Generate all combinations of 6 additional cities from 1 to 10, excluding the depot
combinations = itertools.combinations(range(1, 10), 6)

def find_min_cycle(comb):
    # Start the path at the depot
    comb = [0] + list(comb)
    min_tour = None
    min_cost = float('inf')
    # Permutate all cities in the combination including the depot
    for perm in itertools.permutations(comb):
        if perm[0] == 0:  # Ensure the tour starts with the depot
            tour_cost = 0
            # Sum up the cost of this permutation path
            for i in range(len(perm)-1):
                tour_cost += distances[(perm[i], perm[i+1])]
            tour_cost += distances[(perm[-1], 0)]  # Return to the depot
            
            # Check if this is the shortest path found yet
            if tour_cost < min_cost:
                min_cost = tour_cost
                min_tour = list(perm) + [0]  # Return path to the depot
            
    return min_tour, min_cost

# Check all combinations to find the best tour
best_tour = None
best_cost = float('inf')

for comb in combinations:
    tour, cost = find_min_cycle(comb)
    if cost < best_cost:
        best_cost = cost
        best_tou = tour

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")