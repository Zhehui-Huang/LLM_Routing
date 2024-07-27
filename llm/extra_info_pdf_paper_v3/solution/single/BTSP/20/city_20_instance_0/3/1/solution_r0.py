import math
import sys

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(cities):
    n = len(cities)
    tour = []
    visited = set()
    current_city = 0  # Start at the depot
    tour.append(current_city)
    visited.add(current_city)
    
    while len(visited) < n:
        nearest_city = None
        min_distance = float('inf')
        for i in range(n):
            if i not in visited:
                dist = euclidean_distance(cities[current_city], cities[i])
                if dist < min_distance:
                    min_distance = dist
                    nearest_city = i
        current_city = nearest_city
        visited.add(current_city)
        tour.append(current_city)
    
    tour.append(0)  # Return to the depot
    return tour

def calculate_tour_data(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Define the cities coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Obtain a tour from the nearest neighbor heuristic
tour = nearest_neighbor_tour(cities)

# Calculate tour total cost and max distance
total_cost, max_distance = calculate_tour_data(cities, tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")