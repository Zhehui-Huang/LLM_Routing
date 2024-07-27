import math
from itertools import product

# City coordinates index by city number
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Path finding
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []

    # Generate all combinations of picking one city from each group
    for combination in product(*groups):
        # Start from depot, go through one city from each group, and return to depot
        tour = [0] + list(combination) + [0]
        
        # Calculate the distance of this tour
        distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check if the found tour is shorter than the best one we've found so far
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

    return best_tour, min_distance

# Finding the optimal tour
tour, total_cost = find_shortest_tour()

# Output the result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))