import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_edges_and_weights():
    """ Get all edges and their distances in sorted order by distance. """
    edges = []
    for i in cities:
        for j in cities:
            if i != j:  # Ensure no self-loops
                edges.append((i, j, distance(cities[i], cities[j])))
    return sorted(edges, key=lambda x: x[2])

edges_sorted = get_edges_and_weights()

def find_min_bottleneck_tour():
    # Attempt to use each edge as the maximum bottleneck constraint
    for max_dist in sorted(set(edge[2] for edge in edges_sorted)):
        for perm in permutations(list(cities.keys())[1:]):
            path = [0] + list(perm) + [0]
            total_dist, max_edge_dist = 0, 0
            valid_path = True
            # Check the path for validity under the current max_dist
            for i in range(len(path) - 1):
                dist = distance(cities[path[i]], cities[path[i+1]])
                if dist > max_dist:
                    valid_path = False
                    break
                total_dist += dist
                if dist > max_edge_dist:
                    max_edge_dist = dist
            if valid_path:
                return path, total_dist, max_edge_dist

# Find the minimal bottleneck Hamiltonian circuit
tour, total_cost, max_distance = find_min_bottleneck_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)