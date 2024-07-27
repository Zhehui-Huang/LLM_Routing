import math
from itertools import permutations, combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_travel_cost(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))

def find_best_tour(city_combination, cities):
    min_route = None
    min_cost = float('inf')
    for perm in permutations(city_combination):
        # Ensure the tour starts and ends at depot city 0
        route = (0,) + perm + (0,)
        cost = total_travel_cost(route, cities)
        if cost < min_cost:
            min_cost = cost
            min_route = route
    return min_route, min_cost

# Define cities (depot at index 0)
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Get all combinations of 11 cities excluding the depot city
city_indices = list(range(1, 15))  # City indices excluding the depot
combinations_of_cities = combinations(city_eq.indices, 11)  # Choose 11 out of 14 cities

# Include depot city (index 0) and find the best tour
overall_best_route = None
overall_min_cost = float('inf')
for city_combination in combinations_of_cities:
    route, cost = find_best_tour(city_combination, cities)
    if cost < overall_min_cost:
        overall_min_cost = cost
        overall_best_route = route

print("Tour:", list(overall_best_route))
print("Total travel cost:", overall_min_cost)