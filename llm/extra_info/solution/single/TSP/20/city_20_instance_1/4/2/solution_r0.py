import math
from itertools import permutations

# City coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generating permutations of all cities (excluding the depot city 0)
other_cities = list(cities.keys())[1:]
city_permutations = permutations(other_cities)

# Initialize minimal distance large so first calculated will be stored
min_distance = float('inf')
best_tour = None

# Evaluate each possible permutation tours
for perm in city_permitudes:
    # Include the depot city at the start and end of the tour
    tour = [0] + list(perm) + [0]
    # Calculate the cost of this tour
    tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    # Update the minimum distance and best tour found so far
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")