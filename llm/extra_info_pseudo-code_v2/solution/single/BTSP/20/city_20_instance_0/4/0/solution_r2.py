import math
import itertools

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Brute-force search for finding the tour minimizing the maximum edge length
all_cities = range(len(cities))
best_tour = None
best_max_distance = float('inf')

for perm in itertools.permutations(all_cities[1:]):  # Generate permutations excluding the depot
    tour = [0] + list(perm) + [0]  # Start and end at the depot
    max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour

# Calculate the total cost of the best tour
total_travel_cost = sum(calculate_distance(cities[best_tour[i]], cities[best_tour[i + 1]]) for i in range(len(best_tour) - 1))

print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", best_max_distance)