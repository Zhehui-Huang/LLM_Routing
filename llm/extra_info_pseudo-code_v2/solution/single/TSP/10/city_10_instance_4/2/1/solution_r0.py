import math
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

def euclidean_distance(city1, city2):
    # Compute Euclidean distance between two cities given their coordinates
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_total_distance(tour):
    # Calculate the total travel cost of a tour
    total_distance = 0
    number_of_cities = len(tour)
    for i in range(number_of_cities - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def initial_tour():
    # Create an initial tour using nearest-neighbor heuristic starting from the depot city
    start_city = 0
    unvisited_cities = set(range(1, len(coordinates)))  # Exclude the depot initially
    tour = [start_city]
    current_city = start_city

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the depot city
    return tour

# Generate an initial tour
tour = initial_tour()
total_travel_cost = compute_total_distance(tour)

# Output the initial solution
print("Initial Tour:", tour)
print("Initial Total Travel Cost:", total_travel_cost)