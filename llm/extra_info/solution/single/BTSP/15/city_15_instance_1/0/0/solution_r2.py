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

# Generate a matrix of distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def minimize_max_edge_tour():
    best_route = None
    min_max_edge = float('inf')
    total_cost_best = 0
    
    # Permute over all permutations of city indices except for the depot city 0
    for permutation in itertools.permutations(range(1, n)):
        # Append city 0 at the start and the end to complete the round-trip
        route = (0,) + permutation + (0,)
        
        # Calculate the maximum edge length and total cost of the current route
        max_edge = 0
        total_cost = 0
        for i in range(1, len(route)):
            dist = distances[route[i-1]][route[i]]
            total_cost += dist
            if dist > max_edge:
                max_edge = dist
        
        # Update best found route if current has a smaller maximum edge length
        if max_edge < min_max_edge:
            min_max_edge = max_edge
            best_route = route
            total_cost_best = total_cost

    return best_route, total_cost_best, min_max_edge

# Execute the function
tour, total_cost, max_dist = minimize_max_edge_tour()

# Print output according to the specified format
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")