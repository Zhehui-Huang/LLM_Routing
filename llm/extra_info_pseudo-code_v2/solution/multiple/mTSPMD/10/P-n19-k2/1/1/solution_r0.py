import math
import random

# List of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize pheromone levels and heuristic information
def initialize_pheromones(num_cities, init_trail):
    return [[init_trail for _ in range(num_cities)] for _ in range(num_cities)]

def initialize_visibility(num_cities):
    visibility = [[0 if i == j else 1 / distance(i, j)
                   for j in range(num_cities)] for i in range(num_cities)]
    return visibility

# Calculate the transition probabilities
def transition_probabilities(current_city, allowed, pheromone, visibility, alpha, beta):
    denominator = sum((pheromone[current_city][j] ** alpha) * (visibility[current_city][j] ** beta)
                      for j in allowed)
    probabilities = []
    for j in allowed:
        numerator = (pheromone[current_city][j] ** alpha) * (visibility[current_city][j] ** beta)
        probability = numerator / denominator if denominator != 0 else 0
        probabilities.append((j, probability))
    return probabilities