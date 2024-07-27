import itertools
import math

# City coordinates with depot at index 0
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Groups of cities
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def calc_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tour_cost(tour):
    """Calculate the total cost of the specific tour."""
    total_cost = 0
    last_city = tour[0]
    for city in tour[1:]:
        total_cost += calc_distance(cities[last_city], cities[city])
        last_city = city
    return total_cost

# Get all combinations of cities taking one from each city group
possible_tours = list(itertools.product(*city_groups))

# Add the depot city at the beginning and the end of each tour
possible_tours = [[0] + list(tour) + [0] for tour in possible_tours]

# Calculate costs of all tours and find the one with the minimum cost
min_cost = float('inf')
best_tour = None
for tour in possible_tours:
    cost = tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour found and the corresponding cost
print("Tour:", best_tour)
print(f"Total travel cost: {min_cost:.2f}")