import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def calculate_tour_cost(tour, coordinates):
    """Calculate total cost for a given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost