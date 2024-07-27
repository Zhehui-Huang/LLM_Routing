import itertools
import math

# Define cities' coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define city groups
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(city1, city2):
    """ Computes the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_full_path_cost(path):
    """ Computes the total travel cost of the given path, including return to the depot """
    total_cost = 0
    current_city = 0  # starting at the depot
    for city in path:
        total_cost += euclidean_distance(current_city, city)
        current_city = city
    total_cost += euclidean_distance(current_city, 0)  # return to the depot
    return total_cost

# Generate all possible tours
min_cost = float('inf')
best_tour = None

for combination in itertools.product(*groups):
    tour = [0] + list(combination) + [0]  # form the tour starting and ending at depot
    cost = compute_full_path cost(tour[1:-1])  # pass only the non-depot portion of the tour
    if cost < min_cost:
        min_cost = cost
        best_tour = tour
        
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")