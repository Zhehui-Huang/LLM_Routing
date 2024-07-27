import math
import itertools

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate distance matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def minimize_max_edge_tour():
    best_route = None
    min_max_edge = float('inf')
    total_cost_best = 0

    for route in itertools.permutations(range(1, n)):
        route = (0,) + route + (0,)
        max_edge = 0
        total_cost = 0
        for i in range(1, len(route)):
            dist = distances[route[i-1]][route[i]]
            total_cost += dist
            if dist > max_edge:
                max_edge = dist
        if max_edge < min_max_edge:
            min_max_edge = max_edge
            best_route = route
            total_cost_best = total_cost

    return best_route, total_cost_best, min_max_edge

# Finding optimal tour
tour, total_cost, max_dist = minimize_max_edge_tour()
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")