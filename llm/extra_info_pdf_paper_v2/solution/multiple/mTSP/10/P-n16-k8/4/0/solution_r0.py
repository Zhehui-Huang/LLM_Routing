import numpy as np
from itertools import permutations
from math import sqrt

# City coordinates and robot information
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

num_robots = 8

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial random tours
np.random.seed(0)
cities_indices = list(range(1, 16))  # Exclude depot
np.random.shuffle(cities_indices)

# Divide cities into roughly equal parts for initial robot tours, not optimized and requires further intelligent distribution
city_chunks = np.array_split(cities_indices, num_robots)

# Function to compute a tour cost
def tour_cost(tour):
    total_cost = 0
    current_city = 0  # Start and end at depot
    for city in tour:
        total_cost += distance(cities[current_city], cities[city])
        current_city = city
    total_cost += distance(cities[current_city], cities[0])  # Return to depot
    return total_cost

# Compute and output each robot's tour and cost
overall_total_cost = 0
for i, chunk in enumerate(city_chunks):
    tour = [0] + list(chunk) + [0]
    cost = tour_cost(chunk)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")