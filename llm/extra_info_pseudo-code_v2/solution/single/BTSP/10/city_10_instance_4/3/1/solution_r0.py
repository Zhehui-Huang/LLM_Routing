import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_biconnected_subgraph(vertices, edges):
    # Sorting edges based on the weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    biconnected_edges = []
    for edge in sorted_edges:
        biconnected_edges.append(edge)
        if is_biconnected(vertices, biconnected_edges):
            return biconnected_edges
    return []

def is_biconnected(vertices, edges):
    # Creating a simplistic check for biconnection by ensuring all nodes have at least two connections
    from collections import defaultdict
    connection_count = defaultdict(int)
    for edge in edges:
        connection_count[edge[0]] += 1
        connection_count[edge[1]] += 1
    return all(count >= 2 for count in connection_count.values())

def calculate_path_cost(tour, coords):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coords[tour[i-1]], coords[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

def approximate_btsp_tour(coords):
    # Generate all edges with distances
    vertices = list(range(len(coords)))
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(vertices, 2)]

    # Apply heuristic to find a biconnected subgraph
    biconnected_edges = find_biconnected_subgraph(vertices, edges)

    # Assuming a fully connected graph, simply find a Hamiltonian path that uses all vertices
    # This is a simplification and should normally be solved using a more complex method
    tour = [0]  # Starting at depot city 0
    visited = set(tour)
    while len(visited) < len(coords):
        current = tour[-1]
        next_city = min((e for e in biconnected_edges if e[0] == current or e[1] == current and e[0] not in visited and e[1] not in visited), key=lambda x: x[2])
        if next_city[0] == current:
            tour.append(next_city[1])
        else:
            tour.append(next_city[0])
        visited.add(tour[-1])
    tour.append(0)  # Return to the depot

    total_cost, max_distance = calculate_path_cost(tour, coords)
    return tour, total cost, max_distance

# Define the coordinates of the cities
coordinates = [
    (79, 15),  # Depot
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

tour, total_cost, max_distance = approximate_btsp_tour(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)