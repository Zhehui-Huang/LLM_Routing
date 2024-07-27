import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute Euclidean Distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
num_cities = len(cities)
distance_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')  # No self-loop

# Heuristic: Try nearest neighbor strategy as a base
def nearest_neighbor_tour(start=0):
    unvisited = set(range(1, num_cities))
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to depot city
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i - 1]][tour[i]]
    return cost

# Perform nearest neighbor heuristic
tour = nearest_neighbor_tour()
tour_cost = calculate_tour_cost(tour)

print("Tour:", tour)
print("Total travel cost:", tour_cost)