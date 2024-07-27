import math
from itertools import combinations

# Given cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate all pairwise distances
distances = {}
for c1, c2 in combinations(cities.keys(), 2):
    dist = euclidean_distance(c1, c2)
    distances[(c1, c2)] = dist
    distances[(c2, c1)] = dist

# Adding self-loop with distance 0 for completeness
for i in cities:
    distances[(i, i)] = 0

# Nearest Neighbor Heuristic modified to prioritize maximum edge minimization for BTSP
def nearest_neighbor_btsp(start, distances):
    unvisited = set(cities.keys())
    tour = [start]
    max_edge = 0
    
    current = start
    unvisited.remove(current)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[(current, city)])
        max_edge = max(max_edge, distances[(current, next_city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Closing the loop
    tour.append(start)
    max_edge = max(max_edge, distances[(current, start)])
    
    total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    return tour, total_cost, max_edge

# Compute BTSP using the heuristic
tour, total_cost, maximum_distance = nearest_neighbor_btsp(0, distances)

# Output results according to the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", maximum_distance)