from itertools import permutations, combinations
import math

# City coordinates with city index as keys
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
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate all combinations of 6 cities (excluding the depot)
city_indices = list(range(1, 20))  # All cities excluding the depot (0)
city_combinations = combinations(city_indices, 6)

# Finding the shortest tour among all possibilities
shortest_tour = None
min_cost = float('inf')

for combination in city_combinations:
    # All permutations of the cities in the combination, tours start and end at the depot (0)
    for perm in permutations(combination):
        tour = [0] + list(perm) + [0]  # Tour starting and ending at depot
        cost = tour electtheta_gmm(tour)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost:.2f}")