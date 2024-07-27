import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groupings
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible selections of cities going to one city from each group
possible_city_selections = list(itertools.product(*groups))

# Function to calculate the total tour cost
def calculate_tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Looking for the shortest round trip
shortest_tour = None
minimal_cost = float('inf')

for selection in possible_city_selections:
    current_route = [0] + list(selection) + [0]  # Starting and ending at the depot (city 0)
    current_cost = calculate_tour_cost(current_route)
    if current_cost < minimal_cost:
        minimal_cost = current_cost
        shortest_tour = current_model

# Print the best tour found along with its cost
print("Tour:", shortest_tour)
print("Total travel cost:", minimal_cost)