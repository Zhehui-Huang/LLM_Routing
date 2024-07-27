import math
from itertools import product

# City coordinates
cities = [
    (8, 11),   # Depot city 0
    (40, 6),   # Group 0
    (95, 33),  # Group 1
    (80, 60),  # Group 0
    (25, 18),  # Group 2
    (67, 23),  # Group 0
    (97, 32),  # Group 1
    (25, 71),  # Group 1
    (61, 16),  # Group 1
    (27, 91),  # Group 2
    (91, 46),  # Group 2
    (40, 87),  # Group 0
    (20, 97),  # Group 1
    (61, 25),  # Group 0
    (5, 59),   # Group 0
    (62, 88),  # Group 1
    (13, 43),  # Group 2
    (61, 28),  # Group 2
    (60, 63),  # Group 2
    (93, 15)   # Group 0
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour based on the Euclidean distance."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate all possible tours starting and ending at the depot (0) and visiting one city from each group
possible_tours = []
for combination in product(*groups):
    possible_tours.append([0] + list(combination) + [0])

# Find the shortest tour from all possible tours
shortest_tour = None
min_cost = float('inf')

for tour in possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour

# Display results
print("Tour:", shortest_tour)
print("Total travel_cost:", min_cost)