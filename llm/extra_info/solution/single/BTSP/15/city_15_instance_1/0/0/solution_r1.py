import math
import itertools

# Define city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate the distance matrix
n = len(cities)
distance_matrix = [[euclidean_separation(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def find_tour_minimizing_max_edge():
    best_route = None
    min_max_edge = float('inf')
    best_total_cost = 0

    for permutation in itertools.permutations(range(1, n)):  # Permute through all cities except the depot (city 0)
        route = (0,) + permutation + (0,)  # Start and end at the depot city 0
        local_max_edge = 0
        total_cost = 0
        for i in range(1, len(route)):
            dist = distance_matrix[route[i-1]][route[i]]
            total_cost += dist
            if dist > local_max_edge:
                local_max_edge = dist
        if local_max_edge < min_max_edge:
            best_route = route
            min_max_edge = local_max_edge
            best_total_cost = total_cost

    return best_route, best_total_cost, min_max_edge

# Execute the function and print the results
tour, total_cost, max_dist = find_tour_minimizing_max_edge()
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")