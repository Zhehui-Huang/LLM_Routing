import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def is_biconnected(n, edges):
    # Create adjacency matrix
    graph = csr_matrix((n, n))
    for i, j, w in edges:
        graph[i, j] = graph[j, i] = w
    # Using scipy to find number of connected components
    n_components = connected_components(csgraph=graph, directed=False, return_labels=False)
    return n_components == 1

def find_tour(n, coords):
    # Step 0: Initialize
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(range(n), 2)]
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Step 1: Find a bottleneck-optimal biconnected subgraph
    E_BB = []
    index = 0
    while not is_biconnected(n, E_BB):
        E_BB.append(sorted_edges[index])
        index += 1

    # Step 2: Identify a tour
    # Create graph from E_BB
    graph = csr_matrix((n, n))
    for i, j, w in E_BB:
        graph[i, j] = graph[j, i] = w
    T = minimum_spanning_tree(graph).toarray().astype(int)
    tour = [0]  # Starting at the depot city 0
    visited = {0}
    current = 0
    
    # Construct the tour by traversing the minimum spanning tree
    while len(visited) < n:
        neighbors = [(j, T[current, j]) for j in range(n) if T[current, j] > 0 and j not in visited]
        if neighbors:
            next_city, _ = min(neighbors, key=lambda x: x[1])
            tour.append(next_city)
            visited.add(next_city)
            current = next_city
        
    tour.append(0)  # Return to the depot city

    # Compute the total cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = euclidean_distance(coords[tour[i]], coords[tour[i + 1]])
        total_cost += d
        max_distance = max(max_distance, d)

    return tour, total_cost, max_distance

# Cities coordinates
cities_coords = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
                 (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
                 (28, 49), (91, 94), (51, 58), (30, 48)]

n = len(cities_coords)
tour, total_cost, max_distance = find_tour(n, cities_coords)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")