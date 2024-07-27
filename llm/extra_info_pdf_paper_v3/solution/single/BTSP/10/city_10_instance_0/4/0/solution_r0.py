import itertools
import math

# Coordinates of the cities indexed from 0 to 9
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_metrics(permutation):
    total_cost = 0
    max_distance = 0
    tour = [0] + list(permutation) + [0]
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return tour, total_cost, max_distance

def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    tour_cost = None
    
    # Generate all permutations for cities 1 to 9, starting and ending at 0
    for permutation in itertools.permutations(range(1, 10)):
        tour, total_cost, max_distance = calculate_tour_metrics(permutation)
        if max_distance < min_max_distance:
            min_max_trav = max_distance
            optimal_tour = tour
            tour_cost = total_cost
            min_max_distance = max_distance
    
    return optimal_tour, tour_cost, min_max_distance

# Calculate the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")