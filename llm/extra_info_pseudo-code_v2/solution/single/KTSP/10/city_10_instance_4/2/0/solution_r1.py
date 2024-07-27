import math
import random

# ------------------ Code Continued with Definitions ------------------

# Distance calculation between two cities using Euclidean distance
def euclidean_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Precompute distances between each pair of cities
def precompute_distances(cities):
    distances = {}
    for i in cities:
        for j in cities:
            distances[(i, j)] = euclidean_dist(cities[i], cities[j])
    return distances

# Generate Initial Solution: A random tour starting and ending at the depot, including exactly k cities
def generate_initial_solution(cities, k):
    city_ids = list(cities.keys())
    random.shuffle(city_ids)
    city_ids.remove(0)
    tour = [0] + city_ids[:k-1] + [0]
    return tour

# Calculate total distance of the tour
def calculate_total_distance(tour, distances):
    total_distance = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_distance

# Shake function: Perform random swaps in the tour to generate a new neighbor
def shake(tour, k):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    return [0] + new_tour[:k-1] + [0]

# Local Search function: Swap cities to find a better solution
def local_search(tour, distances):
    min_distance = calculate_total_distance(tour, distances)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_distance = calculate_total_distance(new_tour, distances)
            if new_distance < min_distance:
                best_tour = new_tour[:]
                min_distance = new_distance
    return best_tour

# GVNS algorithm
def gvns(cities, k, itermax, pmax):
    distances = precompute_distances(cities)
    best_solution = generate_initial_solution(cities, k)
    best_cost = calculate_total_distance(best_solution, distances)
    
    for _ in range(itermax):
        current_solution = shake(best_solution, k)
        for _ in range(pmax):
            new_solution = local_search(current_solution, distances)
            new_cost = calculate_total_error_distance(new_solution, distances)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                break
    
    return best_solution, best_cost

# Main execution
k = 8
itermax = 100
pmax = 10
best_tour, best_cost = gvns(cities, k, itermax, pmax)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)