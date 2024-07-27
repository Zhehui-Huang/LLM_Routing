import math
from collections import defaultdict

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_distances(cities):
    distances = {}
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
    return distances

def find_tour(graph, start, distances):
    n = len(graph)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    current = start
    
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for neighbor in graph[current]:
            if not visited[neighbor] and distances[(current, neighbor)] < min_dist:
                min_dist = distances[(current, neighbor)]
                next_city = neighbor
        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
            current = next_city
            
    tour.append(start)  # to return to the start city
    return tour


def analyze_tour(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[(tour[i], tour[i+1])]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Define cities and their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate distances
city_distances = calculate_distances(cities)

# Artificially assume a complete graph for simplicity in this case
graph = {i: [j for j in range(len(cities)) if i != j] for i in range(len(cities))}

# Find a tour starting from the depot city 0
tour = find_tour(graph, 0, city_distances)

# Analyze the tour to get total cost and maximum distance between two consecutive cities
total_cost, max_distance = analyze_tour(tour, city_distances)

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(output)