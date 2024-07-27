import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate all possible tours starting and ending at the depot (city 0)
def generate_tours():
    # All cities except the depot
    city_list = list(cities.keys())[1:]
    for perm in permutations(city_list):
        # Adding depot at the start and the end
        yield [0] + list(perm) + [0]

# Finding the best tour that minimizes the maximum distance between successive cities
best_tour = None
min_max_distance = float('inf')
best_total_cost = 0

for tour in generate_tours():
    max_leg_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        leg_distance = distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_data = leg_distance
    if max_leg_data < min_max_distance:
        min_max_distance = max_leg_data
        best_total_cost = total_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")