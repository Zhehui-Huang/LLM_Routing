import math
import random

# Define the coordinates for each city including the depot
cities = [
    (3, 26), # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49),
    (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a random feasible solution (initial tour)
def generate_random_tour():
    tour = list(range(1, len(cities)))  # start with all cities except the depot
    random.shuffle(tour)
    return [0] + tour + [0]  # start and end at the depot

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Try to find a better tour by swapping two cities
def two_opt(tour):
    best_cost = calculate_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # no need to swap consecutive cities
                new_tour = tour[:]
                new_tour[i:j+1] = tour[j:i-1:-1]
                new_cost = calculate_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
        tour = best_tour
    
    return best_tour, best_cost

# Generate an initial random tour
initial_tour = generate_random_tour()
initial_cost = calculate_cost(initial_tour)

# Improve the tour using the 2-opt method
optimal_tour, optimal_cost = two_opt(initial_tour)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)