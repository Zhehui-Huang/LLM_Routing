import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def k_tsp_heuristic(cities, k):
    # Initial setup
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    
    # Choose subsets of cities, leaving out exactly two cities (as we have 10 and need 8)
    min_tour = None
    min_cost = float('inf')
    city_indices = list(range(1, n))  # excluding the depot initially
    for subset in permutations(city_indices, k-1):
        current_tour = [0] + list(subset) + [0]  # start and end at the depot
        cost = calculate_total_distance(current_tour, distance_matrix)
        if cost < min_cost:
            min_tour = current_tour
            min_cost = cost

    return min_tour, min_cost

# Cities coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# We include the depot city 0 in the count, so we need to visit 8 in total.
tour, total_cost = k_tsp_heuristic(cities, 8)

# Results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))