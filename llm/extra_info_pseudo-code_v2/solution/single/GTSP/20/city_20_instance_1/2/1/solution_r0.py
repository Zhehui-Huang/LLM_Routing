import math
import random

# City coordinates indexed by city index
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# City groups
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

def distance(A, B):
    """Calculate Euclidean distance between two cities given by their indices."""
    x1, y1 = cities[A]
    x2, y2 = cities[B]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def construct_initial_tour(groups, depot):
    """ Randomly construct an initial feasible tour starting and ending at depot """
    tour = [depot]
    for group in groups.values():
        tour.append(random.choice(group))
    tour.append(depot)  # closing the tour back to the depot
    return tour

def calculate_tour_cost(tour):
    """ Calculate the total cost of a given tour """
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Get an initial tour
initial_tour = construct_initial_tour(groups, 0)
initial_tour_cost = calculate_tour_cost(initial_tour)

# Output
print("Tour:", initial_tour)
print("Total travel cost:", initial_tour_cost)