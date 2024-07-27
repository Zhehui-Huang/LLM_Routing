import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
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

# Number of cities to visit (including the depot)
k = 7

# Identify the nearest 'k-1' cities to the depot city
depot = cities[0]
distances = [(euclidean_distance(depot, cities[i]), i) for i in range(1, len(cities))]
distances.sort()

# Take the closest k-1 cities plus the depot city
chosen_cities = [0] + [idx for _, idx in distances[:k-1]]

# Generate all permutations of the chosen cities (excluding the depot at start and end)
min_tour = None
min_cost = float('inf')

for perm in permutations(chosen_cities[1:]):
    tour = [0] + list(perm) + [0]
    cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")