import math
import random

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize and generate a random tour
def generate_initial_tour(num_cities):
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    return [0] + tour + [0]

# Calculate the total travel cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Perform the 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: 
                    continue
                if distance(tour[i], tour[i-1]) + distance(tour[j+1], tour[j]) > distance(tour[i], tour[j+1]) + distance(tour[i-1], tour[j]):
                    best[i:j+1] = reversed(best[i:j+1])
                    improved = True
    return best

# Find a good tour using a heuristic approach
def find_tour(num_cities, epochs=1000):
    best_tour = generate_initial_tour(num_cities)
    best_cost = calculate_total_cost(best_tour)
    for _ in range(epochs):
        new_tour = generate_initial_tour(num_cities)
        new_tour = two_opt(new_tour)
        new_cost = calculate_total_cost(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
    return best_tour, best_cost

# Get the best tour using the Lin-Kernighan type heuristic approach
num_cities = len(coordinates)
best_tour, best_cost = find_tour(num_cities)

# Outputting the result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)