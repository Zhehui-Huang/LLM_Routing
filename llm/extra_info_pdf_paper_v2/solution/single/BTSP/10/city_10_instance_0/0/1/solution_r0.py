import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City coordinates
coordinates = [
    (50, 42),  # City 0 - Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Number of cities
n = len(coordinates)

# Precompute the distance matrix
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(*coordinates[i], *coordinates[j])

# Implement simple heuristic for BTSP
def find_btsp_tour():
    # Placeholder heuristic: minimal nearest neighbor algorithm
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(0)  # return to depot
    
    # Calculate total travel cost and bottleneck distance
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_travel_cost += dist
        max_distance = max(max_distance, dist)
    
    return tour, total_travel_cost, max_distance

# Get tour and calculations
tour, total_travel_cost, max_distance = find_btsp_tour()

# Output the required results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_travel_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_distance:.2f}')