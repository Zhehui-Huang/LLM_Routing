import math
from itertools import combinations
import networkx as nx

# Cities coordinates
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        G.add_node(i, pos=cities[i])
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def heuristic_tsp(G):
    # Create Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(G)

    # Find odd degree vertices
    odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

    # Create Minimum Weight Perfect Matching for odd degree vertices
    subgraph = nx.subgraph(G, odd_vertices)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Add matching edges to the MST
    mst.add_edges_from(min_weight_matching)

    # Construct an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

    # Convert the Eulerian circuit to a Hamiltonian path
    visited = set()
    path = []
    cost = 0
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
        cost += G[u][v]['weight']

    # Ensuring the tour ends at the starting point (Depot city 0)
    if path[-1] != path[0]:
        path.append(path[0])
        cost += G[path[-1]][path[0]]['weight']

    return path, cost

# Main computation
graph = create_graph(cities)
tour, total_cost = heuristic_tsp(graph)

# Print the result
print("Tour:", tour)
print("Total travel cost:", total_cost)