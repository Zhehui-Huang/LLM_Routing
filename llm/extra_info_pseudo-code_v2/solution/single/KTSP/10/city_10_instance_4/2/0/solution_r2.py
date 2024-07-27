import math
import random

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two city coordinates
def euclidean_dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances for all city pairs
def precompute_distances():
    distances = {}
    for i in cities:
        for j in cities:
            distances[(i, j)] = euclidean_dist(cities[i], cities[j])
    return distances

distances = precompute_distances()

# Generate an initial random solution with exactly k cities
def generate_initial_solution(k):
    tour = [0] + random.sample(list(cities.keys())[1:], k-1) + [0]
    return tour

# Calculate the total tour distance
def calculate_tour_distance(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Shaking by swapping two random cities in the tour
def shake(tour, shk_level):
    new_tour = tour[1:-1]
    for _ in range(shk_level):
        i, j = random.sample(range(len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return [0] + new_tour + [0]

# Local improvement using two-level strategy: Swap and 2-Opt
def local_search(tour, lsc_level):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if lsc_level == 1 or i > 1:  # Swap
                    new_tour = tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+1:]
                else:  # 2-Opt
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_distance(new_tour)
                if new_cost < calculate_tour_distance(tour):
                    tour = new_tour
                    improved = True
    return tour

# GVNS algorithm
def gvns(k, max_iter, shake_level, local_search_level):
    best_tour = generate_initial_solution(k)
    best_cost = calculate_tour_distance(best_tour)

    for _ in range(max_iter):
        current_tour = shake(best_tour, shake_level)
        current_tour = local_search(current_tour, local_search_level)
        current_cost = calculate_tour_distance(current_tour)

        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost

    return best_tour, best_cost

# Parameters
k = 8
max_iter = 100
shake_level = 3
local_search_level = 1

best_tour, best_cost = gvns(k, max_iter, shake_level, local_search_level)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)