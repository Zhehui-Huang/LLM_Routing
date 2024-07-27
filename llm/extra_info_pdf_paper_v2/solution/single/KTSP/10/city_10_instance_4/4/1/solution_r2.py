import random
from math import sqrt

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities based on their coordinates."""
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, cities):
    """Calculate the total distance of a tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def local_search(tour, cities):
    """Local search to try improving the tour by swapping pairs of cities and checking if it improves the total distance."""
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = calculate_total_distance(new_tour, cities)
                if new_distance < best_distance:
                    best_tour, best_distance = new_tour[:], new_distance
                    improved = True
    return best_tour, best_distance

def solve_k_tsp(cities, k):
    """Main function to solve the k-TSP by using random sampling and local optimization."""
    city_indices = list(range(1, len(cities)))
    best_global_tour = None
    best_global_distance = float('inf')
    for _ in range(100):  # Number of random starts
        random_subset = random.sample(city_indices, k - 1)
        initial_tour = [0] + random_subset + [0]
        tour, distance = local_search(initial_tour, cities)
        if distance < best_global_distance:
            best_global_tour, best_global_distance = tour, distance
    return best_global_tour, best_global_distance

# Define cities as given in the prompt
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Invoke solver to determine the best tour and its cost
best_tour, best_total_distance = solve_k_tsp(cities, 8)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")