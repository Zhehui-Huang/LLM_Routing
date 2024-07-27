import random
import itertools
from copy import deepcopy

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(1, len(tour)):
        total_dist += distance_matrix[tour[i-1]][tour[i]]
    total_dist += distance_matrix[tour[-1]][tour[0]]
    return total_dist

def generate_random_subset(all_cities, k, depot):
    subset = {depot}
    while len(subset) < k:
        subset.add(random.choice(list(all_cities - subset)))
    return list(subset)

def find_shortest_tour(subset):
    best_tour = None
    best_distance = float("inf")
    for permutation in itertools.permutations(subset):
        if permutation[0] == 0:  # Ensure starting from the depot
            current_distance = calculate_total_distance(permutation)
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = permutation
    return best_tour, best_distance

def multi_start_k_tsp():
    all_cities = set(range(len(cities)))
    best_global_tour = None
    best_global_distance = float("inf")
    number_of_iterations = 1000  # Number of random starts
    
    for _ in range(number_of_iterations):
        subset = generate_random_subset(all_cities, 12, 0)  # Including the depot
        tour, distance = find_shortest_tour(subset)
        if distance < best_global_distance:
            best_global_distance = distance
            best_global_tour = list(tour) + [tour[0]]  # To return to the starting city

    return best_global_tour, best_global_distance

# Run the multi start k-TSP heuristic
best_tour, best_total_cost = multi_start_k_tsp()

# Outputting the result
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)