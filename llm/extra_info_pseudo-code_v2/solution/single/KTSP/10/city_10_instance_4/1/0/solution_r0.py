import random
import math
from itertools import permutations, combinations

# Position data for the cities
positions = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

def euclidean_distance(city1, city2):
    return math.sqrt((positions[city1][0] - positions[city2][0]) ** 2 + (positions[city1][1] - positions[city2][1]) ** 2)

def total_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))