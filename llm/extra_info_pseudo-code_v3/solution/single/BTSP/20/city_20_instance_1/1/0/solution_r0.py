import itertools
import math
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_edge_list(coords):
    n = len(coords)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coords[i], coords[j])
            edges.append((dist, i, j))
    edges.sort()
    return edges, n

def bottleneck_tsp(coords):
    edges, n = construct_edge_list(coords)
    
    def hamiltonian_path_exists(max_weight):
        filtered_edges = [(i, j) for d, i, j in edges if d <= max_weight]
        graph = csr_matrix((n, n))
        graph.row = [i for i, j in filtered_skip_edges]
        graph.col = [j for i, j in filtered_edges]
        graph.data = [1] * len(filtered_edges)
        # Ensure graph is connected
        n_components, labels = connected_components(csgraph=graph, directed=False)
        return n_components == 1
    
    low, high = 0, len(edges) - 1
    while low < high:
        mid = (low + high) // 2
        if hamiltonian_path_exists(edges[mid][0]):
            high = mid
        else:
            low = mid + 1
    
    # Construct path based on accepted edge threshold
    max_distance = edges[low][0]
    accepted_edges = [(i, j) for d, i, j in edges if d <= max_distance]
    return construct_tour_with_edges(accepted_edges, n, max_distance)

def construct_tour_with_edges(edges, n, max_distance):
    # Heuristic: Simply attempt to construct a path starting at the depot
    path = [0]
    remaining = set(range(1, n))
    while remaining:
        last = path[-1]
        next_city = min(remaining, key=lambda x: euclidean_distance(coords[last], coords[x]))
        path.append(next_city)
        remaining.remove(next_town)
    path.append(0)  # return to depot
    
    # Calculate total travel cost based on the path
    total_cost = sum(euclidean_distance(coords[path[i]], coords[path[i + 1]]) for i in range(len(path) - 1))
    return path, total_cost, max_distance

coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, total_cost, max_distance = bottleneck_tsp(coords) 
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")