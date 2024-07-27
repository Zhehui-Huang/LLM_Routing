import math
from itertools import combinations

# City coordinates (index is the city number)
cities = [
    (8, 11),  # City 0 (Depot)
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calculate_all_distances(cities):
    """Calculate Euclidean distances between all city pairs."""
    n = len(cities)
    distances = {}
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist
    return distances

city_distances = calculate_all_distances(cities)