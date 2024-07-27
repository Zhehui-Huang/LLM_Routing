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
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# All cities excluding the depot
all_cities = list(cities.keys())[1:]
min_cost = float('inf')
best_tour = None

# Test all permutations of the cities (brute-force approach)
for perm in itertools.permutations(all_cities):
    # Adding depot at start and end of the permutation
    tour = (0,) + perm + (0,)
    # Calculate the total travel cost of this tour
    cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    # Update minimum cost and tour
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Display the results
print("Tour:", list(best_tour))
print("Total travel cost:", round(min_tf cost, 2))