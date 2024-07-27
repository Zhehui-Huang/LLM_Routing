import itertools
import math

# City data and groups as specified
cities = [
    (14, 77),  # Depot city 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Precompute all the necessary distances
dist = { (i, j): distance(cities[i], cities[j]) for i in range(20) for j in range(20) }

# Find the shortest tour that visits one city from each group & returns to depot
best_cost = float('inf')
best_tour = None

# Iterate over all permutations of one city from each group
for choice in itertools.product(*groups):
    # We must also consider all permutations of the choices from the groups
    for perm in itertools.permutations(choice):
        # Always include the depot (city 0) at the start and end
        tour = [0] + list(perm) + [0]
        cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

# Output the solution
print(f"Tour: {best_t-our}")
print(f"Total travel cost: {best_cost:.2f}")