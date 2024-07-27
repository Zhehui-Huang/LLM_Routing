import math
import networkx as nx

# Define functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_complete_graph(points):
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            G.add_edge(i, j, weight=euclidean_distance(points[i], points[j]))
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def create_multigraph(T, M):
    H = nx.MultiGraph(T)
    for (u, v) in M:
        H.add_edge(u, v, weight=G[u][v]['weight'])
        H.add_edge(v, u, weight=G[u][v]['weight'])  # Ensure the graph is symmetric
    return H

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H, source=0))

def create_hamiltonian_circuit(circuit, start_vertex):
    visited = set()
    path = [start_vertex]
    for u, v in circuit:
        if v not in visited:
            visited.add(v)
            path.append(v)
    path.append(start_vertex)  # Complete the circuit
    return path

# Define points based on city coordinates
points = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Constructing the model and solving
G = create_complete_graph(points)
T = find_minimum_spanning_tree(G)
O = find_odd_degree_vertices(T)
M = minimum_weight_perfect_matching(G, O)
H = create_multigraph(T, M)
circuit = find_eulerian_circuit(H)
tour = create_hamiltonian_circuit(circuit, 0)

# Calculate total travel cost
total_cost = sum(euclidean_distance(points[tour[i]], points[tour[i+1]]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")