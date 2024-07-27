import numpy as np
import random

# Cities coordinates
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
    19: (19, 72)
}

# Distance calculation function
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate random initial solutions
def random_solution():
    nodes = list(cities.keys())
    nodes.remove(0)  # Remove the depot city for now
    random.shuffle(nodes)
    nodes = [0] + nodes[:12] + [0]  # We select 12 random cities plus the depot at the start and end
    return nodes

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simple heuristic Multiple Random Start
def multiple_random_start(n_iterations=1000):
    best_tour = None
    best_cost = float('inf')
    for _ in range(n_iterations):
        tour = random_solution()
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Finding the best tour for conditions
best_tour, best_cost = multiple_random_start(10000)  # Set to 10,000 iterations for a more thorough search

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")