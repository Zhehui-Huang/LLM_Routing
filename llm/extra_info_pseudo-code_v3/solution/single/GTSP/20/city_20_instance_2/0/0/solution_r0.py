import math
import itertools

# City coordinates: index corresponds to city number
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Groupings of the cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    # Generate all permutations of selecting one city from each group
    for group_selections in itertools.product(*groups):
        all_possible_routes = itertools.permutations(group_selections)
        
        for route in all_possible_routes:
            route_with_depot = [0] + list(route) + [0]  # Start and end at the depot
            total_distance = sum(calculate_distance(route_with_depot[i], route_with_depot[i+1]) for i in range(len(route_with_depot) - 1))
            
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = route_with_depot

    return best_tour, min_distance

tour, total_cost = find_shortest_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")