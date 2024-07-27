import itertools
import math

cities_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    x1, y1 = cities_coords[city1]
    x2, y2 = cities_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_best_route():
    min_distance = float('inf')
    best_route = []

    # Generate combinations of 6 additional cities plus the depot
    for cities in itertools.combinations(range(1, len(cities_coords)), 6):
        current_route = [0] + list(cities) + [0]
        
        # Generate permutations of the chosen 7 cities, starting and ending at depot
        for permutation in itertools.permutations(current_route[1:-1]):
            route = [0] + list(permutation) + [0]
            distance = sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

            if distance < min_distance:
                min_distance = distance
                best_route = route

    return best_route, min_distance

# Execute the function and format the output
tour, total_cost = find_best_route()
print("Tour:", tour)
print("Total travel cost:", total_cost)