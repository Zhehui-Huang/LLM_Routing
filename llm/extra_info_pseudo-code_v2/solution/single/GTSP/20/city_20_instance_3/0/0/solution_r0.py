import math
from itertools import permutations

# City coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour():
    """ Find the shortest tour visiting one city from each group """
    all_group_combinations = list(permutations([0] + [g[0] for g in groups]))
    min_cost = float('inf')
    best_tour = None

    for group_order in all_group_combinations:
        for permutation in permutations(group_order[1:]):  # Permute cities within groups
            tour = [0] + list(permutation)
            tour.append(0)
            cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Execute the function and print the result
best_tour, total_cost = find_shortest_tour()
print(f"Tour: {best_tour}\nTotal travel cost: {total_cost:.2f}")