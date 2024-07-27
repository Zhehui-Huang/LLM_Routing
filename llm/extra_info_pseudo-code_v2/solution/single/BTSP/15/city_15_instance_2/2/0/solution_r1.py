import numpy as np
import math

# Cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Euclidean Distance Calculation
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = calculate_distance(cities[i], cities[j])

# Nearest neighbor heuristic to minimize maximum distance between consecutive cities in the tour
def find_tour():
    unvisited = set(range(1, num_cities))
    tour = [0]
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to depot
    
    # Calculate maximum distance between consecutive cities and total travel cost
    max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_dist

# Executing function to find the tour
tour, total_cost, max_dist = find_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")