import math
from itertools import permutations

# Defined cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial tour (simply visiting cities in numerical order and returning to depot)
initial_tour = list(cities.keys()) + [0]

# Compute total distance of a given tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Display initial tour and its total distance
print("Initial Tour:", initial_tweeks, "Total Travel Cost:", total_distance(initial_tour))