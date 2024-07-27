import math
from sys import maxsize

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def initialize_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_min_bottleneck_tour(cities):
    num_cities = len(cities)
    distances = initialize_distances(cities)
    visited = [False] * num_cities
    tour = [0]
    visited[0] = True
    current_city = 0
    
    max_edge_length = 0
    total_distance = 0

    # Choose next city to minimize the bottleneck until all cities are visited
    while len(tour) < num_cities:
        next_city = -1
        min_bottleneck = maxsize
        for i in range(num_cities):
            if not visited[i] and distances[current_city][i] < min_bottleneck:
                next_city = i
                min_bottleneck = distances[current_city][i]
        
        visited[next_city] = True
        tour.append(next_city)
        total_distance += min_bottleneck
        max_edge_length = max(max_edge_length, min_bottleneck)
        current_city = next_city
    
    # Close the loop back to the depot
    final_leg_distance = distances[current_city][0]
    total_distance += final_leg_distance
    max_edge_length = max(max_edge_length, final_leg_distance)
    tour.append(0)

    return tour, total_distance, max_edge_length

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Compute the tour, total travel cost, and max consecutive distance
tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour(cities)

print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))