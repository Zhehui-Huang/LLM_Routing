import itertools
import math

# City coordinates with indices
cities = {
    0: (79, 15),   # Depot city
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

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities, indexed by their keys in the cities dict. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(route):
    """ Calculate the total distance for the route, including return to the starting city. """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(route[i], route[i+1])
    total_distance += euclidean_distance(route[-1], route[0])  # returning to the depot
    return total_distance

# Generate all combinations of 7 additional cities (excluding the depot)
city_indices = list(cities.keys())[1:]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
min_distance = float('inf')
best_tour = None

for combination in itertools.combinations(city_indices, 7):
    current_route = [0] + list(combination) + [0]  # Start and end at the depot
    current_distance = calculate_total_distance(current_route)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_route

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")