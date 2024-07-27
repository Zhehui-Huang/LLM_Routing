import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Coordinates of cities
coordinates = [
    (8, 11),    # City 0 - Depot
    (40, 6),    # City 1
    (95, 33),   # City 2
    (80, 60),   # City 3
    (25, 18),   # City 4
    (67, 23),   # City 5
    (97, 32),   # City 6
    (25, 71),   # City 7
    (61, 16),   # City 8
    (27, 91),   # City 9
    (91, 46),   # City 10
    (40, 87),   # City 11
    (20, 97),   # City 12
    (61, 25),   # City 13
    (5, 59),    # City 14
    (62, 88),   # City 15
    (13, 43),   # City 16
    (61, 28),   # City 17
    (60, 63),   # City 18
    (93, 15)    # City 19
]

# Distance matrix calculation
n = len(coordinates)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

# All cities except the depot
non_depot_cities = list(range(1, n))

# We need to start and end at the depot, and include exactly 4 cities in the tour, including the depot
min_cost = float('inf')
best_tour = []

# Generate all combinations of 3 non-depot cities
for cities in itertools.combinations(non_depot_cities, 3):
    tour_cities = [0] + list(cities) + [0]
    # Generate all permutations of the selected cities excluding the start and end city
    for perm in itertools.permutations(tour_cities[1:-1]):
        current_tour = [0] + list(perm) + [0]
        # Calculate cost
        current_cost = sum(dist_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        # Update best tour if current is better
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)