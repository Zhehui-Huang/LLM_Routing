import math
import random

# City coordinates: index corresponds to city number
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Groups of cities
groups = {
    0: [1, 2, 5, 6], 1: [8, 9, 10, 13], 2: [3, 4, 7], 3: [11, 12, 14]
}

def euclidean_dist(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_initial_tour(city_groups, depot):
    """Creates a random initial tour visiting one city from each group and returning to depot."""
    tour = [depot]
    for group in city_groups.values():
        tour.append(random.choice(group))
    tour.append(depot)  # return to depot
    return tour