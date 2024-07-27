import math
import itertools

# Coordinates of cities including the depot
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Grouped cities by the problem statement
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_shortest_tour(groups):
    """ Find the shortest tour that visits one city from each group starting and ending at depot """
    depot = 0
    min_tour_cost = float('inf')
    best_tour = None
    
    # Generate all possible configurations for choosing one city from each group
    for combination in itertools.product(*groups):
        full_tour = [depot] + list(combination) + [depot]
        tour_cost = 0
        
        # Calculate the tour cost
        for i in range(len(full_tour) - 1):
            tour_cost += calculate_distance(full_tour[i], full_tour[i + 1])
        
        # Check if this tour is better than the best found so far
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = full_tour
            
    return best_tour, min_tour_cost

# Compute the tour
tour, total_cost = find_shortest_tour(groups)

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)