import math
import random

# City coordinates as given in the problem statement 
cities = {
    0: (9, 93),   1: (8, 51),   2: (74, 99),  3: (78, 50),
    4: (21, 23),  5: (88, 59),  6: (79, 77),  7: (63, 23),
    8: (19, 76),  9: (21, 38),  10: (19, 65), 11: (11, 40),
    12: (3, 21),  13: (60, 55), 14: (4, 39)
}

# Euclidean distance
def dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Total tour cost for a sequence of cities
def tour_cost(tour):
    return sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))