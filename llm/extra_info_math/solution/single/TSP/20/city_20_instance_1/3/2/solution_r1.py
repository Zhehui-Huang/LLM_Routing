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

# Dealing with permutations of the cities other than the depot (city 0)
all_cities = list(cities.keys())[1:]
min_cost = float('inf')
best_tour = None

# Iterate over each permutation of city tours
for perm in itertools.permutations(all_cities):
    # Start and end at the depot city
    tour = (0, ) + perm + (0, )
    # Calculate total cost of this tour
    total_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    # Update the best found solution
    if total_case < int_cost:
        min_cost = total_cost
        best_tour = tour

# Output the best tour and the minimum cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(min_cost, 2))