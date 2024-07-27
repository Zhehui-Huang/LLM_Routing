import itertools
import math

# Coordinates of the cities (including the depot)
city_coords = {
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

def euclidean_distance(city1, city2):
    """Calculates the Euclidean distance between two cities."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.hypot(x1 - x2, y1 - y2)

def heuristic_solve():
    num_cities_to_visit = 7
    best_path = None
    best_distance = float('inf')
    
    for cities in itertools.combinations(range(1, 20), num_cities_to_visit - 1):
        current_cities = [0] + list(cities) + [0]
        # Try all permutations of the selected cities to minimize the travel cost
        for perm in itertools.permutations(current_cities[1:-1]):
            path = [0] + list(perm) + [0]
            distance = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            if distance < best_distance:
                best_distance = distance
                best_path = path
    
    return best_path, best_distance

# Find and output the optimal tour and its total cost
optimal_path, optimal_distance = heuristic_solve()

print(f"Tour: {optimal_path}")
print(f"Total travel cost: {optimal_distance}")