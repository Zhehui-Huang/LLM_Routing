import math
import itertools

# Define the cities and their coordinates
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
    14: (21, 77),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Consider all permutations of the cities (except depot city 0)
all_cities = list(cities.keys())[1:]
city_permutations = itertools.permutations(all_cities)

# Variable to track the minimum cost and the corresponding tour
min_cost = float('inf')
best_tour = None

# Check every possible permutation to find the optimal route
for perm in city_permutations:
    perm = (0,) + perm + (0,)  # Starting and ending at the depot city
    total_cost = sum(calc_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = perm

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", round(min_cost, 2))