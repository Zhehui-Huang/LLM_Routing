import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def create_complete_graph(node_coordinates):
    G = nx.Graph()
    nodes = range(len(node_coordinates))
    for u, v in combinations(nodes, 2):
        G.add_edge(u, v, weight=euclidean_distance(node_coordinates[u], node_coordinates[v]))
    return G


def find_odd_degree_nodes(T):
    return [v for v, d in T.degree() if d % 2 == 1]


def christofides_algorithm(node_coordinates):
    G = create_complete_graph(node_coordinates)
    MST = nx.minimum_spanning_tree(G)
    odd_degree_nodes = find_odd_degree_nodes(MST)
    subgraph = G.subgraph(odd_degree_nodes)
    minimum_weight_matching = max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    H = MST.copy()
    for u, v in minimum_weight_matching:
        H.add_edge(u, v, weight=G[u][v]['weight'])
    
    euler_circuit = list(eulerian_circuit(H, source=0))
    
    # Convert Eulerian circuit to Hamiltonian circuit
    visited = set()
    path = []
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(0)  # to return to the starting city
    
    # Calculate total travel cost
    total_travel_cost = 0
    for i in range(len(path) - 1):
        total_travel_cost += G[path[i]][path[i+1]]['weight']
        
    return path, total_travel_cost

# City coordinates based on the problem statement
node_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]
tour, cost = christofides_algorithm(node_coordinates)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")