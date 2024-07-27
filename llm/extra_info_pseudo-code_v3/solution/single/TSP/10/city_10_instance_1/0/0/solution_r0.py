import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_complete_graph(points):
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
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
    G = nx.MultiGraph(T)
    G.add_edges_from(M)
    return G

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(eulerian_circuit, start_vertex):
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(start_vertex)  # adding the start vertex to complete the circuit
    return tour

# Defining points based on the city coordinates
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

# Step by step applying Christofides algorithm
G = create_complete_network(points)
T = find_minimum_spanning_tree(G)
O = find_odd_degree_vertices(T)
M = minimum_weight_perfect_matching(G, O)
H = create_multigraph(T, M)
circuit = find_eulerian_circuit(H)
tour = create_hamiltonian_circuit(circuit, 0)

# Calculating the total travel cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))

# Printing the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")