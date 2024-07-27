import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)  # Using Euclidean distance formula

# Define city coordinates
cities = [
    (90, 3),  # Depot city 0
    (11, 17), (7, 27), (95, 81), (41, 54),
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

# Define city groups
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]