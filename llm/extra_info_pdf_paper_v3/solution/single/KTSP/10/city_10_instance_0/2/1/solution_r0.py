import itertools
import math

# City coordinates (index corresponds to city number)
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points p1 and p2 """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the shortest possible tour that involves exactly 4 cities including the depot city 0
min_cost = float('inf')
best_tour = []

# Get all combinations of three cities other than the depot
for combo in itertools.combinations(range(1, 10), 3):
    # Always include city 0 (depot) and then compute all permutations of the cities including the depot
    for perm in itertools.permutations(combo):
        # Tours including return to the depot city
        tour = [0] + list(perm) + [0]
        # Calculate total cost of this tour
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Update the best tour if this one has a lower cost
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the solution
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")