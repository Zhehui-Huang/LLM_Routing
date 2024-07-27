import math
from itertools import permutations

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups
groups = {
    '0': [1, 3, 5, 11, 13, 14, 19],
    '1': [2, 6, 7, 8, 12, 15],
    '2': [4, 9, 10, 16, 17, 18]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute the shortest path visiting exactly one city from each group
def find_shortest_path():
    min_distance = float('inf')
    best_tour = None
    
    for group1 in groups['0']:
        for group2 in groups['1']:
            for group3 in groups['2']:
                for perm in permutations([group1, group2, group3]):
                    tour = [0] + list(perm) + [0] # Starting and ending at the depot city 0
                    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
                    if total_distance < min_distance:
                        min_distance = total_distance
                        best_tour = tour

    return best_tour, min_distance

# Execute the function and display results
tour, total_cost = find_shortest_path()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")