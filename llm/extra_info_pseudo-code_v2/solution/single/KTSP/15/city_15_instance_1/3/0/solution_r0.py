import random
import math
from itertools import permutations

# Graph
coords = {
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

# Distance function
def dist(a, b):
    return math.sqrt((coords[a][0] - coords[b][0]) ** 2 + (coords[a][1] - coords[b][1]) ** 2)

# Generate initial solution
def generate_initial_solution(total_cities, k=6):
    cities = list(range(total_cities))
    random.shuffle(cities)
    tour = cities[:k]
    if 0 not in tour:
        tour[0] = 0
    return tour

# Calculate the cost of a given tour
def calculate_tour_cost(tour):
    tour_cost = dist(tour[-1], tour[0])  # Closing the loop
    for i in range(len(tour) - 1):
        tour_cost += dist(tour[i], tour[i + 1])
    return tour_cost

# Iterative improvement
def find_best_tour(allowed_cities, k, num_iterations=10000):
    best_tour = generate_initial_solution(len(allowed_cities), k)
    best_cost = calculate_tour_cost(best_tour)
  
    for _ in range(num_iterations):
        new_tour = best_tour[:]
        # Swap two elements
        idx1, idx2 = random.sample(range(1, k), 2)  # Never swap the depot (index 0)
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
        new_cost = calculate_tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
  
    return best_tour, best_cost

# Select 6 cities including the depot and find the best tour
allowed_cities = list(coords.keys())
best_tour, best_cost = find_best_tour(allowed_cities, 6)

# Returning results
print("Tour:", best_tour + [best_tour[0]])  # Append the depot city to close the tour
print("Total travel cost:", round(best_cost, 2))