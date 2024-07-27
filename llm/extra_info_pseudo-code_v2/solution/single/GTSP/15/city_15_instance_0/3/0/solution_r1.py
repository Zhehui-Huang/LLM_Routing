import math
import itertools

# Coordinates of cities including the depot
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# City groups
groups = [
    [2, 7, 10, 11, 14],   # Group 0
    [1, 3, 5, 8, 13],     # Group 1
    [4, 6, 9, 12]         # Group 2
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour):
    """ Calculate the total cost of the tour """
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def find_best_tour(groups, depot):
    """ Generate all combinations and find the shortest path """
    all_combinations = itertools.product(*groups)
    best_tour = None
    min_cost = float('inf')
    
    for combination in all_combinations:
        tour = [depot] + list(combination) + [depot]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Finding the optimal tour
optimal_tour, optimal_cost = find_best_tour(groups, 0)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)