import math
import random

# Define the coordinates for the depot and other cities
cities = [
    (90, 3),  # Depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a distance matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate an initial random tour
def initial_tour():
    tour = list(range(1, n))  # exclude the depot (city 0 initially)
    random.shuffle(tour)
    return [0] + tour + [0]  # start and end at the depot

# Perform the 2-opt swap to try and improve the tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1:  # Adjacent edges do not swap
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Calculate the total cost of the tour
def tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[j]] for i, j in zip(tour[:-1], tour[1:]))

# Find the best tour using a heuristic approach
def find_best_tour():
    initial = initial_tour()
    optimized = two_opt(initial)
    total_cost = tour_cost(optimized)
    return optimized, total_cost

# Execute the main function to find the best tour
best_tour, best_cost = find_best_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")