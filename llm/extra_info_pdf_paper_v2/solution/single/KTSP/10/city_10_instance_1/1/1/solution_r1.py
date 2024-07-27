from math import sqrt
from itertools import permutations

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_route_cost(route, cities):
    total_cost = 0
    n = len(route)
    for i in range(n - 1):
        total_cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return total_cost

def find_best_route(cities, k):
    # k includes the start and end at the depot, so we need k-2 other cities to visit
    all_cities = list(cities.keys())[1:]  # Remove depot from choices
    best_cost = float('inf')
    best_tour = None
    
    for tour_subset in permutations(all_cities, k - 2):
        full_tour = [0] + list(tour_subset) + [0]  # Start and end at the depot
        cost = calculate_route_cost(full_tour, cities)
        if cost < best_cost:
            best_cost = cost
            best_tour = full_tour
            
    return best_tour, best_cost

# Define the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Find the best tour that visits exactly 5 cities (including the depot)
best_tour, best_cost = find_best_route(cities, 5)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))