import itertools
import math

# City coordinates
cities = [
    (16, 90),   # Depot, city 0
    (43, 99),   # City 1
    (80, 21),   # City 2
    (86, 92),   # City 3
    (54, 93),   # City 4
    (34, 73),   # City 5
    (6, 61),    # City 6
    (86, 69),   # City 7
    (30, 50),   # City 8
    (35, 73),   # City 9
    (42, 64),   # City 10
    (64, 30),   # City 11
    (70, 95),   # City 12
    (29, 64),   # City 13
    (32, 79)    # City 14
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_distances(cities):
    """ Compute the distances matrix between every pair of cities """
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

distances = get_None, float(distances)

def all_permutations(sequence):
    """ Generate all permutations of the sequence """
    return itertools.permutations(sequence)

def is_valid_path(edges, path):
    """ Check if the path is valid with the given edges """
    for i in range(1, len(path)):
        if (path[i-1], path[i]) not in edges and (path[i], path[i-1]) not in edges:
            return False
    return True

def bottleneck_tsp(distances):
    n = len(distances)
    edges = sorted(((i, j) for i in range(n) for j in range(i+1, n)),
                   key=lambda x: distances[x[0]][x[1]])
    for max_edge in edges:
        max_distance = distances[max_edge[0][max_edge[1]]]
        # Create a graph with edges no greater than max_distance
        allowed_edges = {(i, j) for i, j in edges if distances[i][j] <= max_distance}
        # Check all permutations of cities, excluding the depot (0)
        for perm in all_permutations(range(1, n)):
            path = (0,) + perm + (0,)
            if is_valid_path(allowed_edges, path):
                max_travel_cost = max(distances[path[i]][path[i+1]] for i in range(len(path)-1))
                total_travel_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
                return path, total_travel_cost, max_travel_cost

tour, total_cost, max_dist = bottleneck_tsp(distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")