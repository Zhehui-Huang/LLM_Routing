import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_nearest_neighbor(current_city, remaining_cities):
    nearest = None
    min_distance = float('inf')
    for city in remaining_cities:
        distance = euclidean_distance(cities[current_city], cities[city])
        if distance < min_distance:
            min_distance = distance
            nearest = city
    return nearest, min_distance

def nearest_neighbor_tour(start_city, num_cities):
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    remaining_cities = set(cities.keys()) - {start_city}
    
    while len(tour) < num_cities:
        next_city, distance = find_nearest_neighbor(current_city, remaining_cities)
        tour.append(next_city)
        total_distance += distance
        current_city = next_city
        remaining_cities.remove(next_city)
    
    # Returning to the start city
    return_distance = euclidean_distance(cities[current_city], cities[start_city])
    tour.append(start_city)
    total_distance += return_distance
    
    return tour, total_distance

# Use the heuristic to find an approximate solution
tour, total_cost = nearest_neighbor_tour(0, 12)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)