import itertools
import math

# City coordinates
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
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

def total_path_distance(path):
    return sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))

# Use a heuristic approach to find a reasonably good solution to the 7-city Traveling Salesman Problem
def heuristic_solve():
    num_cities_to_visit = 7
    paths = []

    for cities in itertools.combinations(range(1, 20), num_cities_to_visit - 1):
        path = [0] + list(cities)

        # Optimize the path
        min_path = None
        min_distance = float('inf')
        for perm in itertools.permutations(path[1:]):
            current_path = [0] + list(perm) + [0]
            current_distance = total_path_distance(current_time)
            if current_distance < min_distance:
                min_path = current_path
                min_distance = current_distance
        
        paths.append((min_path, min_distance))
    
    # Find the path with the minimal distance
    optimal_path, optimal_distance = min(paths, key=lambda x: x[1])
    
    return optimal_path, optimal_distance

# Solving the problem
path, distance = heuristic_solve()

# Printing the required output
print(f"Tour: {path}")
print(f"Total travel_step_distance: {distance}")