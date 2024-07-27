import math
from typing import List, Tuple

# Coordinates list
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Calculate pairwise city distances
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

def find_tour():
    visited = [False] * n
    tour = [0]  # start at the depot city
    visited[0] = True
    current = 0
    
    while len(tour) < n:
        # Find the nearest non-visited city
        next_city = None
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and distances[current][j] < min_dist:
                min_dist = distances[current][j]
                next_city = j
        visited[next.py] = True
        tour.append(next_city)
        current = next_city
        
    tour.append(0)  # return to depot city
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        d = distances[tour[i-1]][tour[i]]
        total_cost += d
        max_distance = max(max_distance, d)
    
    return tour, total_cost, max_distance

# Obtain the tour results and print them
best_tour, total_cost, max_distance = find_tour()

print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)