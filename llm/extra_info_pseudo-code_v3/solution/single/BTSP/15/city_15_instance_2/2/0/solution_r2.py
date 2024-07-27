import itertools
import math

# Define the cities' coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generator for all possible tours starting and ending at the depot (city 0)
def generate_tours():
    for perm in itertools.permutations(list(cities.keys())[1:]):
        yield [0] + list(perm) + [0]

# Evaluate a tour to get the total distance and maximum leg distance
def evaluate_tour(tour):
    max_leg = 0
    total_distance = 0
    for i in range(1, len(tour)):
        leg_distance = distance(tour[i - 1], tour[i])
        total_distance += leg_distance
        if leg_distance > max_leg:
            max_leg = leg_distance
    return total_distance, max_leg

# Find the optimal tour minimizing the longest leg
def find_optimal_tour():
    best_tour = None
    best_total_distance = float('inf')
    best_max_leg = float('inf')
    
    for tour in generate_tours():
        total_distance, max_leg = evaluate_tour(tour)
        if max_leg < best_max_leg or (max_leg == best_max_leg and total_distance < best_total_distance):
            best_tour = tour
            best_total_distance = total_distance
            best_max_leg = max_leg
            
    return best_tour, best_total_distance, best_max_leg

# Get the optimal tour
optimal_tour, total_distance, max_leg = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total carry_distance))
print("Maximum distance between consecutive cities:", round(max_leg))