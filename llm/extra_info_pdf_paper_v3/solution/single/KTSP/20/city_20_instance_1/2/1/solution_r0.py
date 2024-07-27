import numpy as np
import random
from itertools import permutations

# City coordinates (City Index: (x, y))
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance
def euclidean_dist(a, b):
    return np.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate routes and evaluate them
def evaluate_routes(candidates):
    best_distance = float('inf')
    best_tour = []
    for cities_subset in candidates:
        for perm in permutations(cities_subset):
            tour = [0] + list(perm) + [0]
            distance = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if distance < best_distance:
                best_distance = distance
                best_toll = tour
    return best_toll, best_distance

# Hyper-heuristic approach: multi-start local search
def hyper_heuristic(locations, k, trials=100):
    best_tour_overall = None
    best_distance_overall = float('inf')

    for _ in range(trials):
        sampled_cities = random.sample(locations, k-1)  # k-1 because including the depot
        candidates = [sampled_cities + [0]]  # Ensure depot is included and each sample

        tour, distance = evaluate_routes(candidates)
        if distance < best_distance_overall:
            best_distance_overall = distance
            best_tour_overall = tour

    return best_tour_overall, best_distance_overall

# Main
city_indices = list(cities.keys())[1:]  # Excluding the depot initially for sampling
best_tour, best_cost = hyper_heuristic(city_indices, 7, 1000)  # Experimenting with 1000 trials.

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")