from itertools import product
import math

# Define the coordinates of the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define the city groups
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible routes taking one city from each group plus the depot
def find_shortest_tour():
    all_routes = product(*city_groups)
    min_distance = float('inf')
    best_tour = None
    
    # Iterate over all possible combinations of chosen cities (one per group)
    for route in all_routes:
        for permutation in itertools.permutations(route):
            # Always start and end at the depot
            full_route = [0] + list(permutation) + [0]
            # Calculate the total travel cost of the round-trip route
            total_distance = sum(calc_distance(full_route[i], full_route[i+1]) for i in range(len(full_aroute)-1))
            
            # Check if the found tour is better than the current best
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = full_route
                
    return best_tour, min_distance

# Function execution—finding the shortest tour
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)