import math

# Cities coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Euclidean distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Matrix to hold distances between all pairs of cities
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = dist(cities[i], cities[j])

# Simple heuristic for TSP: nearest neighbor
def nearest_neighbor_tour(start):
    unvisited = set(range(n))
    tour = []
    current = start
    tour.append(current)
    unvisited.remove(current)
    tour_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour_cost += distance_matrix[current][next_city]
        current = next_city
        tour.append(current)
        unvisited.remove(current)

    # Returning to the starting point (depot)
    tour_cost += distance_matrix[current][start]
    tour.append(start)

    return tour_cost, tour

# Get a tour solution
tour_cost, tour = nearest_neighbor_tour(0)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", tour_cost)