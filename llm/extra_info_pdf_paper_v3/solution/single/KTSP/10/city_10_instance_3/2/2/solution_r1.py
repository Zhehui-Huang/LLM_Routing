import math
import itertools
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate total path cost
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Function to find the shortest path among all permutations of selected cities
def find_shortest_tour(cities_subset):
    shortest_tour = None
    min_cost = float('inf')
    for perm in itertools.permutations(cities_subset):
        current_tour = [0] + list(perm) + [0]  # Start and end at depot
        current_cost = calculate_total_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour
    return shortest_tour, min_cost

# Multi-start heuristic to sample different subsets
def multi_start_heuristic(number_of_starts=500):
    best_tour, best_cost = None, float('inf')
    for _ in range(number_of_starts):
        # Randomly selecting 6 additional cities
        selected_cities = random.sample(range(1, 10), 6)
        tour, cost = find_shortest_tour(selected_cities)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Applying the multi-start heuristic
tour, total_cost = multi_start_heuristic(500)  # will test with 500 starts
print("Tour:", tour)
print("Total travel cost:", total_cost)