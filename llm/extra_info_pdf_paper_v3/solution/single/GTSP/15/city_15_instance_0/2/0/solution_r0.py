import math
from itertools import product

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours
def generate_tours():
    min_tour = None
    min_cost = float('inf')
    
    # Product of city choices from each group
    for combination in product(groups[0], groups[1], groups[2]):
        tour = [0] + list(combination) + [0]
        cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    
    return min_tour, min_cost

# Find the optimal tour and its cost
optimal_tour, optimal_cost = generate_tours()

# Output
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))