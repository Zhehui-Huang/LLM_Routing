import math
from itertools import product

# Coordinates of cities including the depot city 0
coordinates = [
    (8, 11),   # Depot City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate a full matrix of distances between each pair of cities
distances = [[0] * len(coordinates) for _ in range(len(coordinates))]
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def total_tour_cost(tour):
    """Calculate total tour cost for a given tour."""
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def find_best_tour():
    """Find the best tour that visits one city from each group and returns to the depot."""
    min_cost = float('inf')
    best_tour = []
    
    for combination in product(*groups):
        tour = [0] + list(combination) + [0]
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Execute the find_best_tour function to get the optimal tour and its cost
tour, cost = find_best_tour()

# Output the solution
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))