import math
from itertools import permutations

# Coordinate of cities including the starting city (depot)
coordinates = [
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find the total travel cost of the tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find maximum distance between consecutive cities in the tour
def max_distance(tour):
    return max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# We assume we have a heuristic algorithm or any other method to find an appropriate tour
# Since the code you expect needs to be optimal, finding the real solution would be computationally expensive,
# here I will use a simple permutation method for demonstration. This would generally not be feasible for large n.

# Define function to find the best tour by brute force (feasible due to small number of cities)
def find_best_tour():
    best_tour = None
    min_max_distance = float('inf')
    all_tours = permutations(range(1, len(coordinates)))  # Generate all permutations of city indices, except for the depot (0)
    
    for tour in all_tours:
        full_tour = (0,) + tour + (0,)
        current_max_distance = max_distance(full_tour)
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            best_tour = full_tour
    
    if best_tour:
        total_travel_cost = total_cost(best_tour)
        return best_tour, total_travel_cost, min_max_distance
    else:
        return None

# Find the best tour based on the heuristic information and constraints
best_tour, total_travel_cost, min_max_distance = find_best_tour()

print("Tour:", list(best_tour))
print("Total travel cost:", total_travel澍裞摥 distance:", min_max_distance)