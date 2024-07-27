import numpy as np
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_complete_graph(coords):
    n = len(coords)
    graph = {}
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(coords[i], coords[j])
            graph[(i, j)] = distance
            graph[(j, i)] = distance
    return graph, n

def find_odd_degree_vertices(tree, n):
    degree = np.zeros(n, dtype=int)
    for (i, j), w in tree.items():
        degree[i] += 1
        degree[j] += 1
    odd_vertices = [i for i in range(n) if degree[i] % 2 == 1]
    return odd_vertices

def find_minimum_weight_perfect_matching(odd_vertices, graph):
    subgraph = {(u, v): graph[(u, v)] for u in odd_vertices for v in odd_features if v > u and (u, v) in graph}
    g = nx.Graph()
    for (u, v), w in subgraph.items():
        g.add_edge(u, v, weight=w)
    matching = nx.algorithms.matching.min_weight_matching(g, maxcardinality=True, weight='weight')
    return matching

def create_eulerian_multigraph(tree, matching, n):
    multigraph = nx.MultiGraph()
    multigraph.add_nodes_from(range(n))
    for (i, j), w in tree.items():
        multigraph.add_edge(i, j, weight=w)
    for i, j in matching:
        multigraph.add_edge(i, j, weight=graph[(i, j)])
    return multigraph

def find_eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

def make_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            circuit.append(u)
            visited.add(u)
    circuit.append(circuit[0])
    return circuit

def calculate_total_distance(circuit, graph):
    total_distance = 0
    for i in range(len(circuit) - 1):
        u, v = circuit[i], circuit[i + 1]
        total_distance += graph[(u, v)]
    return total_distance

# Cities coordinates
coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

graph, n = create_complete_graph(coords)

# Step 2: Finding Minimum Spanning Tree
mst = minimum_spanning_tree(squareform(pdist(coords, metric='euclidean')))
mst = mst.toarray()
tree = {(i, j): mst[i, j] for i in range(n) for j in range(n) if mst[i, j] > 0}

# Step 3: Find odd degree vertices
odd_vertices = find_odd_degree_vertices(tree, n)

# Step 4: Minimum weight perfect matching
matching = find_minimum_weight_perfect_matching(odd_vertices, graph)

# Step 5: Create multi-graph H
multigraph = create_eulerian_multigraph(tree, matching, n)

# Step 6: Eulerian circuit
eulerian_circuit = find_eulerian_circuit(multigraph)

# Step 7: Hamiltonian circuit
tour = make_hamiltonian_circuit(eulerian_circuit)

# Step 8: Calculate cost
cost = calculate_total_distance(tour, graph)

print("Tour:", tour)
print("Total travel cost:", cost)