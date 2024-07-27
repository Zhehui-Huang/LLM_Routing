import itertools
import math

# City coordinates
cities = {
    0: (35, 40),  # Depot city
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

# City groups
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their IDs """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_shortest_tour():
    """ Tries all permutations of one city from each group and computes the shortest tour """
    permutations = itertools.product(*groups)
    minimal_tour_length = float('inf')
    best_tour = None

    for perm in permutations:
        # Build a full path including the return to the depot
        path = [0] + list(perm) + [0]
        tour_length = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path)-1))
        
        if tour_length < minimal_tour_length:
            minimal_tour_length = tour_length
            best_tour = path

    return best_tour, minimal_tour_length

# Find the optimal tour and its length
optimal_tour, optimal_length = find_shortest_tour()

# Printing the output
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_length, 2))