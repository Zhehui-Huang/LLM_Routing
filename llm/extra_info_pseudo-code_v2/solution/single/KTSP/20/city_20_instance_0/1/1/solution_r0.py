import numpy as np
from itertools import permutations
from random import sample, randint

# Define the cities
cities = {
    0: (8, 11),   1: (40, 6),   2: (95, 33),  3: (80, 60),
    4: (25, 18),  5: (67, 23),  6: (97, 32),  7: (25, 71),
    8: (61, 16),  9: (27, 91),  10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59),  15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Number of cities to visit including depot
k = 4

# Euclidean distance
def distance(city1, city2):
    return np.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

# Total cost of tour
def tour_cost(tour):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Generate the initial solution
def generate_initial_solution():
    chosen = [0]  # start at depot
    while len(chosen) < k:
        next_city = sample([ci for ci in cities if ci not in chosen], 1)[0]
        chosen.append(next_city)
    chosen.append(0)  # return to depot
    return chosen

# Shake by exchanging one city
def shake(tour):
    internal_tour = tour[1:-1]  # Ignore depot in the beginning and end
    i, j = sample(range(len(internal_tour)), 2)
    internal_tour[i], internal_tour[j] = internal_tour[j], internal_tour[i]
    return [0] + internal_tour + [0]

# Variable Neighborhood Descent (VND)
def vnd(tour):
    improved = True
    while improved:
        improved = False
        all_tours = [tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+1:] for i in range(1, k - 1) for j in range(i + 1, k)]
        best_local_tour = min(all_tours, key=tour_cost)
        if tour_cost(best_local_tour) < tour_cost(tour):
            tour = best_local_tour
            improved = True
    return tour

# GVNS algorithm
def gvns(max_iter=100):
    s = generate_initial_solution()
    best_solution = s
    best_cost = tour_cost(s)
    for _ in range(max_iter):
        sp = shake(s)
        spp = vnd(sp)
        if tour_cost(spp) < best_cost:
            best_solution = spp
            best_cost = tour_cost(spp)
    return best_solution, best_cost

# Execute the algorithm
best_solution, best_cost = gvns()

# Output the results
print(f"Tour: {best_solution}")
print(f"Total travel cost: {round(best_cost, 2)}")