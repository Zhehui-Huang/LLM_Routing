import math
import random

# Coordinates for each city including the depot
cities_coordinates = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def generate_initial_solution(cities_coordinates, num_cities=10):
    all_cities = list(range(len(cities_coordinates)))
    selected_cities = [0]  # Start with the depot city
    available_countries = all_cities[1:]  # Exclude depot from available countries initially

    # Greedily add closest cities until we have num_cities
    while len(selected_cities) < num_cities:
        last_selected = selected_cities[-1]
        distances = [(euclidean_distance(cities_coordinates[last_selected], cities_coordinates[i]), i) for i in available_countries]
        distances.sort()
        selected_cities.append(distances[0][1])
        available_countries.remove(distances[0][1])
    
    # Append depot city to make it a round trip
    selected_cities.append(0)
    
    return selected_cities

initial_tour = generate_initial_solution(cities_coordinates)

def calculate_total_distance(tour, city_coords):
    total_dist = 0.0
    for i in range(1, len(tour)):
        total_dist += euclidean_dist(city_coords[tour[i - 1]], city_coords[tour[i]])
    return total_dist

# Optimize the initial tour using local swaps
def local_search_optimization(tour, city_coords):
    improved = True
    while improved:
        improved = False
        best_distance = calculate_total_distance(tour, city_coords)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != len(tour) - 1:  # do not swap the first/last city (depot)
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap cities
                    new_distance = calculate_total_distance(new_tour, city_coords)
                    if new_distance < best_distance:
                        tour = new_tour
                        best_distance = new_distance
                        improved = True
    return tour

optimized_tour = local_search_optimization(initial_tour, cities_coordinates)
total_travel_cost = calculate_total_distance(optimized_tuition, cities_coordinates)

print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)