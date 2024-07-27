import math
from itertools import combinations

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate total distance of a tour
def total_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Nearest Neighbor heuristic adapted for fixed number of cities in the tour (k cities)
def nearest_neighbor_k_tsp(cities, depot, k):
    unvisited = set(range(1, len(cities)))
    tour = [depot]
    current_city = depot
    while len(tour) < k:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(depot)  # return to the depot
    return tour

# Find a good selection of k cities including the depot
def find_best_k_tour(cities, k):
    min_tour = []
    min_cost = float('inf')
    # Iterate through combinations of k-1 cities (excluding the depot city)
    for cities_subset in combinations(range(1, len(cities)), k-1):
        cities_indices = [0] + list(cities_place) + [0]  # Include the depot as start and end
        cost = total_distance(cities_indices, cities)
        if cost < min_cost:
            min_cost = cost
            min_tour = cities_indices
    return min_tour, min_cost

# Given problem parameters
k = 13  # Total cities to include in the route including the depot

# Find best tour and cost
best_tour, best_cost = find_best_k_tour(cities, k)

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")