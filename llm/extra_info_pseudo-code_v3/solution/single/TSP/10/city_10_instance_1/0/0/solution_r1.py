import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(points):
    G = nx.Graph()
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(points[i], points[j]))
    return G

def find_minimum_span ining_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def create_multigraph(T, M):
    H = nx.MultiGraph(T)
    for u, v in M:
        H.add_edge(u, v, weight=G[u][v]['weight'])
    return H

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(circuit, start_vertex):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            visited.add(u)
            path.append(u)
    path.append(start_vertex)  # add start vertex to complete the circuit
    return path

# Define coordinates of cities including the depot city
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

G = create_complete_graph(points)
T = find_minimum_spanning_tree(G)
O = find_odd_degree_vertices(T)
M = minimum_weight_perfect_matching(G, O)
H = create_multigraph(T, M)
eulerian_circuit = find_eulerian_circuit(H)
tour = create_hamiltonian_circuit(eulerian_circuit, 0)

total_travel_cost = 0
for i in range(1, len(tour)):
    total_travel_cost += euclidean_distance(points[tour[i-1]], points[tour[i]])

# Output the tour and the total cost of the tour
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_date:.2f}")