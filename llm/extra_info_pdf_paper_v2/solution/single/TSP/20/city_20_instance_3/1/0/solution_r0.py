import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a matrix with distances between each pair of cities
num_cities = len(cities)
distances = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

def total_cost(tour):
    """ Calculate the total travel cost of a tour """
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def two_opt(tour):
    """ Attempt to improve the tour by reversing sections of the route """
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = tour[j:i-1:-1]  # This reverses the section from i to j
                if total_cost(new_tour) < total_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Create an initial random tour
initial_tour = list(range(1, num_cities))  # All cities except the depot
random.shuffle(initial_tour)
initial_tour = [0] + initial_tour + [0]  # Starting and ending at the depot

# Optimize the tour
optimized_tour = two_opt(initial_tour)

# Calculate the total distance of the optimized tour
final_cost = total_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", final_cost)