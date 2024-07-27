import math
from heapq import heappop, heappush

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start, points):
    n = len(points)
    visited = [False] * n
    visited[start] = True
    tour = [start]
    current_city = start
    total_cost = 0
    
    for _ in range(1, n):
        next_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city]:
                dist = euclidean_distance(points[current_city], points[city])
                if dist < min_distance:
                    min_distance = dist
                    next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        current_city = next_city
    
    # Going back to the starting point
    return_to_start_distance = euclidean_distance(points[current_city], points[start])
    total_cost += return_to_start_distance
    tour.append(start)
    
    return tour, total_cost

# Coordinates of each city including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the TSP tour using Nearest Neighbor heuristic starting from the depot city 0
tour, total_cost = nearest_neighbor_tour(0, coordinates)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")