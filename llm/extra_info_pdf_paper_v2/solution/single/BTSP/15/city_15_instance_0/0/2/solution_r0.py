import math
from itertools import combinations

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_tour(cities):
    n = len(cities)
    distances = {}
    
    # Calculate all pairwise distances
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

    # Initial setup: start from the depot
    tour = [0]
    visited = set(tour)
    max_distance = 0
    total_cost = 0

    # Greedy approach to visit all cities exactly once
    while len(tour) < n:
        last = tour[-1]
        next_city = None
        min_dist = float('inf')
        
        for i in range(n):
            if i not in visited and distances[(last, i)] < min_dist:
                min_dist = distances[(last, i)]
                next_city = i
        
        tour.append(next_city)
        visited.add(next_city)
        total_cost += min_dist
        max_distance = max(max_distance, min_dist)
    
    # Closing the tour back to the depot
    return_to_depot = distances[(tour[-1], 0)]
    tour.append(0)
    total_cost += return_to_depot
    max_distance = max(max_distance, return_to_depot)
    
    return tour, total_cost, max_distance

# City coordinates
cities = [
    (9, 93),   # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Get the tour results
tour, total_cost, max_distance = find_tour(cities)

# Output the result as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")