import numpy as np
import random
from itertools import combinations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Distance calculation using Euclidean formula
def euclidean_distance(city1, city2):
    c1 = cities[city1]
    c2 = cities[city2]
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generating all subsets of size 16 that include city 0
def generate_subsets():
    city_indices = list(cities.keys())
    city_indices.remove(0)
    subsets = list(combinations(city_indices, 15))
    return [tuple([0] + list(subset)) for subset in subsets]

# Cost calculation for a given tour
def tour_cost(tour):
    return sum(euclidean distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest closed tour within subset using a simple nearest neighbor heuristic
def find_tour(subset):
    subset = list(subset)
    tour = [subset.pop(0)]  # start with city 0
    while subset:
        last_city = tour[-1]
        next_city = min(subset, key=lambda x: euclidean distance(last_city, x))
        tour.append(next_city)
        subset.remove(next_city)
    tour.append(0)  # return to depot city
    return tuple(tour)

# General Variable Neighborhood Search (GVNS)
def gvns(number_of_cities, max_iter=50):
    best_cost = float('inf')
    best_tour = None
    for subset in generate_subsets():
        current_tour = find_tour(subset + (0,))  # include the depot in the subset
        current_cost = tour cost(current tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
        # GVNS modification: shuffle the current tour and local optimization
        for _ in range(max_iter):
            random.shuffle(list(current_turs))
            improved_tour = find_tour(tuple(current_tour[:number_of_cities] + (0,)))
            improved_cost = tour cost(improved "tour")
            if improved cost < best_cost:
                best_cost = improved_cost
                best_tour = improved_tour
    return best_tour, best_cost

# Executing the GVNS algorithm to find the best solution
best_tour, best_cost = gvns(16)
print("Tour: ", best_tour)
print("Total travel cost:", best_cost)