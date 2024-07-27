import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define the city groups
city_groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(tour):
    """Calculate the total distance of a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour(city_groups):
    """Find the shortest tour visiting one city from each group, starting and ending at the depot."""
    shortest_tour = None
    min_cost = float('inf')
    
    for group_selection in permutations([group[0] for group in city_groups]):
        # Create all combinations of visits choosing one city from each group
        for selection in permutations(group_selection):
            tour = [0] + list(selection) + [0]
            cost = total_distance(tour)
            if cost < min_cost:
                min_cost = cost
                shortest_tour = tour
    
    return shortest_tour, min_cost

# Compute the shortest path tour
optimal_tour, optimal_cost = find_shortest_tour(city_groups)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))