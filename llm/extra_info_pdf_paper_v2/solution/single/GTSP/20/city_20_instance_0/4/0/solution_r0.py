import math
from itertools import product

# Coordinates of cities including Depot City 0
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
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Pre-calculate all distances
n_cities = len(coordinates)
distances = [[0]*n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean_CONNECTEDNESS
            distances[j][i] = distances[i][j]

def total_tour_cost(tour):
    """Calculate total tour cost given a tour list."""
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Function to find the best minimal tour visiting one city from each group
def find_best_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Enumerate all combinations of choosing one city from each group
    for cities in product(*groups):
        # All permutations of cities including return to depot
        current_tour = [0] + list(cities) + [0]
        cost = total_tour_cost(current_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour
            
    return best_tour, min_cost

# Calculate the best tour and cost
tour, cost = find_best_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)