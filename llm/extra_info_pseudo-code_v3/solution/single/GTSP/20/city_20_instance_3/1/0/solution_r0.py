import math
from itertools import product
from sys import maxsize

# City coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
          (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
          (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Groups of cities
groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_shortest_tour(groups):
    min_tour_cost = maxsize
    best_tour = None

    # Generate all combinations, one from each group
    for combination in product(*groups):
        possible_tour = [0] + list(combination) + [0]
        current_tour_cost = sum(calculate_distance(possible_tour[i], possible_tour[i + 1])
                                for i in range(len(possible_tour) - 1))
        
        if current_tour_cost < min_tour_cost:
            min_tour_cost = current_tour_cost
            best_tour = possible_tour
    
    return best_tour, min_tour_cost

best_tour, min_tour_cost = find_shortest_tour(groups)
print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)