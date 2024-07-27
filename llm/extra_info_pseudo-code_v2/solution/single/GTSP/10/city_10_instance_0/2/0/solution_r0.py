import math
from itertools import permutations

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of city coordinates
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

# City groups
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

def calculate_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

min_cost = float("inf")
best_tour = []

for perm1 in groups[0]:
    for perm2 in groups[1]:
        for perm3 in groups[2]:
            candidate_tour = [0, perm1, perm2, perm3, 0]
            cost = calculate_total_tour_cost(candidate_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = candidate_tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")