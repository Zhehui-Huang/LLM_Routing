import itertools
import math

# Definition of cities coordinates
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Generate all subsets of 4 cities excluding the depot
city_indices = list(cities.keys())[1:]  # exclude the depot initially
subsets = itertools.combinations(city_indices, 4)

# Evaluate each subset to find the tour with minimal cost
min_cost = float('inf')
best_tour = None

for subset in subsets:
    # Consider all permutations of the selected subset to find the shortest tour
    for perm in itertools.permutations(subset):
        # Tour starting and ending at the depot, through perm cities
        tour = [0] + list(perm) + [0]
        cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Return the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)