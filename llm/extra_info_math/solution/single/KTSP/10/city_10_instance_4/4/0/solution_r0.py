import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the total cost of the given tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Function to find the shortest tour using the nearest neighbor heuristic for a given set of cities plus the depot
def nearest_neighbor_tour(start_city, allowed_cities):
    tour = [start_city]
    current_city = start_city
    while len(tour) < len(allowed_cities):
        next_city = min(
            (city for city in allowed_cities if city not in tour),
            key=lambda city: distance(current_city, city)
        )
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)  # Completing the loop back to the home city
    return tour

# Get all combinations of 7 cities, since we start and end at depot 0 which is already included
city_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)

# Initialize the minimum cost and corresponding tour
minimum_cost = float('inf')
best_tour = None

# Check each combination of 8 cities (home city + 7 others)
for cities_combination in city_combinations:
    selected_cities = [0] + list(cities_combination)  # Always include the depot city
    tentative_tour = nearest_neighbor_tour(0, selected_cities)
    cost = tour_cost(tentative_tour)
    if cost < minimum_cost:
        minimum_cost = cost
        best_tour = tentative_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", minimum_cost)