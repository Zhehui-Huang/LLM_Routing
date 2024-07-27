import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 70),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_shortest_tour():
    # List of all cities except the depot
    city_list = list(cities.keys())[1:]
    best_tour = None
    best_distance = float('inf')
    
    # Generate all possible tours using permutations (Feasible for small number of cities)
    for perm in permutations(city_list):
        # Adding depot to start and end of the tour
        tour = [0] + list(perm) + [0]
        # Calculate the distance of the tour
        distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check if the current tour is shorter than the best found so far
        if distance < best_distance:
            best_tour = tour
            best_distance = distance
    
    return best_tour, best_distance

# Find and output the shortest tour and its distance
tour, total_distance = find_shortest_tour()

print(f"Tour: {tour}")
print(f"Total travel context: {total_distance}")