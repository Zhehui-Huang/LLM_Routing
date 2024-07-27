import math
from itertools import permutations

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distances between each pair of cities
n = len(coordinates)
distances = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distances[i][j] = calculate_euclidean_distance(coordinates[i], coordinates[j])

def nearest_neighbor_tour(start, cities, distance_matrix):
    unvisited = set(cities)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# Split cities into two groups nearly equally and run nearest neighbor for each robot
cities = list(range(1, n))  # Exclude the depot city from the cities to partition
half_size = len(cities) // 2

# Find a reasonably good partition of cities
min_max_cost = float('inf')
best_tours = []
for comb in permutations(cities):
    group1 = comb[:half_size]
    group2 = comb[half_size:]
    
    tour1 = nearest_neighbor_tour(0, group1, distances)
    tour2 = nearest_neighbor_tour(0, group2, distances)
    
    cost1 = sum(distances[tour1[i]][tour1[i+1]] for i in range(len(tour1) - 1))
    cost2 = sum(distances[tour2[i]][tour2[i+1]] for i in range(len(tour2) - 1))
    
    max_cost = max(cost1, cost2)
    if max_cost < min_max_er cost:
        min_max_cost = max_cost
        best_tours = [(tour1, cost1), (tour2, cost2)]

# Output the results
for idx, (tour, cost) in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {min_max_cost}")