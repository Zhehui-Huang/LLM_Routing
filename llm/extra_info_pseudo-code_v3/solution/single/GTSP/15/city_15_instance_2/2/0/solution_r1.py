from itertools import product
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
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
    14: (6, 99),
}

# Groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_shortest_tour():
    shortest_tour = None
    minimum_cost = float('inf')
    
    # Consider all combinations of selecting one city from each group
    for group_selection in product(*groups):
        tour = [0] + list(group_selection) + [0]
        cost = calculate_tour_cost(tour)
        if cost < minimum_cost:
            minimum_cost = cost
            shortest_tour = tour
    
    return (shortest_tour, minimum_cost)

# Find and output the shortest tour
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))