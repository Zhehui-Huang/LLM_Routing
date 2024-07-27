import math
from heapq import heappop, heappush

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city.but taking into
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def find_min_btsp_tour():
    # Starting at the depot city 0
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    max_edge_cost = 0

    # Nearest neighbor approach to generate a tour
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        max_edge_cost = max(max_edge_cost, distance_matrix[current_city][next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Add the return to the start city
    max_edge_cost = max(max_edge_cost, distance_matrix[current_city][0])
    tour.append(0)

    # Calculate total travel cost
    total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_travel_cost, max_edge_cost

# Compute the tour, travel cost and max distance between consecutive cities
tour, total_cost, max_distance = find_min_btsp_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")