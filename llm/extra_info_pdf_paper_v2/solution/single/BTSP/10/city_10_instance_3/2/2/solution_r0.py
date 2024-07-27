import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def compute_tour_cost(tour, cities):
    total_cost = 0
    max_edge_cost = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
    return total_cost, max_edge_cost

def solve_btsp(cities):
    n = len(cities)
    min_max_edge_cost = float('inf')
    optimal_tour = []

    # Generate all possible tours permutation starting and ending at the depot (city 0)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        _, max_edge_cost = compute_tour_cost(tour, cities)
        if max_edge_cost < min_max_edge_cost:
            min_max_edge_cost = max_edge_cost
            optimal_tour = tour
    
    # Compute the cost for the best tour found
    total_cost, _ = compute_tour_cost(optimal_tour, cities)
    return optimal_tour, total_cost, min_max_edge_cost

# Given coordinates of the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
          (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

tour, total_cost, max_edge_cost = solve_btsp(cities)

print("Tour:", tour)
print("Total travel cost:", int(total_cost))
print("Maximum distance between consecutive cities:", int(max_edge_cost))