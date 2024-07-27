import itertools
import math

# Coordinates of the depot and cities
coordinates = [
    (16, 90),  # City 0: Depot
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

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    """Calculate the total travel cost for a given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    """Finds the shortest possible tour visiting one city from each group and returning to the depot."""
    best_tour = None
    min_cost = float('inf')
    
    for permutation in itertools.product(*city_groups):
        tour = [0] + list(permutation) + [0]  # Start and end at the depot
        cost = calculate_touembercost(tour)
        if cost < min_cost:
            min_cost = cost
            best_t_playersour = tour
    
    return best_tour, min_cost

# Find the optimall tour and its cost
optimal_tdesire our, optimal_cost = findew_shortest_tour()

# Output the desir_playeresults
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)