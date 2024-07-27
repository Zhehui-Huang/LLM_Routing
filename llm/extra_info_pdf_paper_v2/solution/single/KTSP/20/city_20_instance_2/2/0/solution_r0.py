import math
import random
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# General Variable Neighborhood Search (GVNS)
def gvns(initial_tour, iterations=1000):
    best_tour = initial_tour
    best_cost = calculate_tour_cost(best_tour)
    
    for _ in range(iterations):
        new_tour = local_search(best_tour)
        new_cost = calculate_tour_cost(new_tour)
        
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
    
    return best_tour, best_cost

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Local search to tweak the tour using swaps
def local_search(tour):
    best_tour = list(tour)
    best_cost = calculate_tour_cost(best_tour)
    for i in range(1, len(tour) - 2):
        for j in range(i+1, len(tour) - 1):
            new_tour = list(best_tour)
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    return best_tour

# Choose 9 other cities randomly besides the depot city
random_cities = random.sample(list(cities.keys() - {0}), 9)

# Create an initial tour starting and ending at the depot
initial_tour = [0] + random_cities + [0]

# Run the GVNS algorithm
final_tour, total_cost = gvns(initial_tour)

# Return the tour and the total cost
print("Tour:", final_tour)
print("Total travel cost:", total_cost)