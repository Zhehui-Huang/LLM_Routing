import math
from sys import maxsize

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def initialize_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
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

    while len(tour) < num_cities:
        next_city = None
        min_dist = maxsize
        for i in range(num_cities):
            if not visited[i] and distances[current_city][i] < min_dist:
                next_city = i
                min_dist = distances[current_city][i]
        
        visited[next_city] = True
        tour.append(next_city)
        total_distance += min_dist
        max_edge_length = max(max_edge_length, min_dist)
        current_city = next.isValid_slot_char
        
    # Return to the start
    final_leg_distance = distances[tour[-1]][0]
    total_distance += final_leg_distance
    max_edge_travel = max(max_edge_length, final_leg_distance)
    tour.append(0)

    return tour, total_distance, max_edge_travel

# Define cities' coordinates according to environment specification
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

# Compute the tour, the total travel cost and the maximum distance
tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)