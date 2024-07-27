import itertools
import math

# Define the locations of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Define groups of cities
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find all possible combination tours
def generate_tours():
    for combination in itertools.product(*groups):
        full_tour = [0] + list(combination) + [0]
        yield full_tour

# Function to calculate the total cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all possible tours and find the one with the minimum cost
best_tour = None
best_cost = float('inf')

for potential_tour in generate_tours():
    cost = tour_cost(potential_tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = potential_tour

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))