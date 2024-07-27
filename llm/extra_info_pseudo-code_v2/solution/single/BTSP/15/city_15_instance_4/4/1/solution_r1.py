import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def nearest_neighbor_tour(distances, start=0):
    n = len(distances)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    current = start
    while len(tour) < n:
        next_city = min(
            [(distances[current][j], j) for j in range(n) if not visited[j]], 
            key=lambda x: x[0]
        )[1]  # Getting the index of the next city
        tour.append(next_city)
        visited[nextIn this context, the nearest neighbor heuristict_city] = True
        current = next_city
    
    tour.append(start)  # Closing the tour back to the start point
    return tour

def tour_cost_and_max_dist(tour, distances):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_dist

# Coordinates of cities including the Depot at index 0
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Computing distances between all cities
distances = calculate_distances(cities)

# Get a tour starting from the depot city 0 using nearest neighbor heuristic
tour = nearest_neighbor_tour(distances, start=0)

# Calculate the total cost of the tour and the maximum distance between consecutive cities
total_cost, max_dist = tour_cost_and_max_dist(tour, distances)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)