import numpy as np
import networkx as nx
import itertools

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with nodes as cities and edges as distances
def create_graph(coordinates):
    G = nx.complete_graph(len(coordinates))
    for i, (x1, y1) in enumerate(coordinates):
        for j, (x2, y2) in enumerate(coordinates):
            if i != j:
                G[i][j]['weight'] = euclidean_distance((x1, y1), (x2, y2))
    return G

# Find the Minimum Spanning Tree using Kruskal's algorithm
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Find minimum cost perfect matching on the subgraph of odd-degree vertices
def minimum_cost_perfect_matching(G, odd_vertices):
    subG = G.subgraph(odd_vertices)
    matching = nx.Graph()
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True, weight='weight')
    matching.add_edges_from(min_weight_matching)
    return matching

# Create an Eulerian circuit from the graph
def eulerian_circuit(G, start_node):
    circuit = list(nx.eulerian_circuit(G, source=start_node))
    return circuit

# Convert Eulerian to Hamiltonian circuit, removing repeated vertices
def eulerian_to_hamiltonian(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Complete the cycle back to the start node
    return path

# Creating the graph with all cities
G = create_graph(coordinates)

# Minimum Spanning Tree
mst = minimum_spanning_tree(G)

# Find vertices with odd degree in MST
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Minimum Cost Perfect Matching on odd degree vertices
matching = minimum_cost_perfect_matching(G, odd_vertices)

# Combine the edges from the MST and the matching to make it Eulerian
augmented_graph = nx.MultiGraph(mst)
augmented_graph.add_edges_from(matching.edges(data=True))

# Find Eulerian circuit in the augmented graph
circuit = eulerian_circuit(augmented_graph, start_node=0)

# Convert Eulerian Circuit to Hamiltonian Circuit
tour = eulerian_to_hamiltonian(circuit)

# Calculate the total travel cost
total_travel_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")