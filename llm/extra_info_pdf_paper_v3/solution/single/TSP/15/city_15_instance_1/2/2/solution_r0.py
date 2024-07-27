import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_mst(G):
    return nx.minimum_spanning_tree(G)

def odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def min_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def eulerian_circuit(G, source):
    return list(nx.eulerian_circuit(G, source=source))

def make_hamiltonian(circuit, G):
    path = []
    visited = set()
    cost = 0
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        # Calculate the cost along the actual tour path
        cost += G[u][v]['weight']
    if path[0] != path[-1]:
        path.append(path[0])
        cost += G[path[-1]][path[0]]['weight']
    return path, cost

# Define the cities
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12),
          (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Step-by-step solution
G = create_graph(cities)
T = find_mst(G)
odd_verts = odd_degree_vertices(T)
matching = min_weight_perfect_matching(G, odd_verts)
T.add_edges_from(matching)
circuit = eulerian_circuit(nx.MultiGraph(T), source=0)
tour, total_cost = make_hamiltonian(circuit, G)

# Output the result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))