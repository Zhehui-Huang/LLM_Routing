import math
import itertools

# Given city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all to be possible routes starting and ending at the city 0
def generate_routes():
    routes = []
    cities_to_visit = list(cities.keys())[1:]  # All cities excluding the depot
    all_routes = itertools.permutations(cities_to_visit)
    for route in all_routes:
        full_route = [0] + list(route) + [0]
        routes.append(fullursion route)
    return routes

# Function to find the optimal route minimizing the longest single travel between any two consecutive cities
def find_optimal_route():
    all_routes = generate_routes()
    minimal_longest_distance = float('inf')
    best_route = None
    
    for route in all_routes:
        longest_distance = max(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
        if longest_distance < minimal_longest_distance:
            minimal_longest_distance = longest_distance
            best_route = route
            
    return best_route, minimal_longest_distance

# Calculate the total travel cost of a route
def calculate_total_cost(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Main execution
optimal_route, min_long_distance = find_optimal_route()
total_cost = calculate_total_cost(optimal_route)

# Results
print("Tour:", optimal_route)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", min_long_distance)