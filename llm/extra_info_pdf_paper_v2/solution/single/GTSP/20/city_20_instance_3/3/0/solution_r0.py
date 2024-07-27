import math
from itertools import permutations

# City coordinates
coordinates = {
    0: (30, 56), # depot
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}
# Group assignment of cities
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate distance matrix
distance_matrix = {}
for i in coordinates.keys():
    for j in coordinates.keys():
        distance_matrix[(i, j)] = euclidean_distance(i, j)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[(tour[i], tour[i + 1])]
    return total_cost

def find_shortest_tour(groups):
    all_possible_tours = []
    
    # Generate all permutations of one city from each group
    for group_selections in permutations([g[0] for g in groups]):
        tour = [0] + list(group_selections) + [0]
        all_possible_tours.append(tour)
    
    # Find the shortest tour
    shortest_tour = None
    min_cost = float('inf')
    for tour in all_possible_tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour

    return shortest_tour, min_cost

shortest_tour, min_cost = find_shortest_tour(groups)

print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)