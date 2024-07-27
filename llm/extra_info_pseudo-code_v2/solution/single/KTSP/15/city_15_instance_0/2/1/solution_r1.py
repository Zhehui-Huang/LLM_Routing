from itertools import combinations
from math import sqrt

# Define the cities with their coordinates
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
    14: (4, 39),
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_best_tour():
    best_cost = float('inf')
    best_tour = None
    
    # Generate all combinations of three cities (besides the depot)
    for comb in combinations([i for i in cities if i != 0], 3):
        current_tour = [0] + list(comb) + [0]  # Starting and ending at the depot city
        cost = total_tour_cost(current_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Getting the best tour and its total cost
best_tour, min_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", min_cost)