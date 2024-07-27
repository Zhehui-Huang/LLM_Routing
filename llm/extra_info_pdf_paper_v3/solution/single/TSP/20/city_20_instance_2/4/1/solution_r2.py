import math
from scipy.spatial import distance_matrix
import networkx as nx

def create_distance_matrix(cities):
    # Calculate Euclidean distance matrix
    dist_matrix = distance_matrix(cities, cities)
    return dist_matrix

def find_minimum_spanning_tree(cities, dist_matrix):
    # Create graph and add weighted edges from the distance matrix
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=dist_matrix[i][j])
            
    # Compute minimum spanning tree using Kruskal's algorithm
    mst = list(nx.minimum_spanning_tree(G, weight='weight').edges(data=True))
    return mst

def find_minimum_cost_perfect_matching(odd_nodes, dist_matrix):
    # Create subgraph with odd degree nodes and their respective distances
    subgraph = nx.Graph()
    for i in odd_nodes:
        for j in odd_nodes:
            if i != j:
                subgraph.add_edge(i, j, weight=dist_matrix[i][j])
    
    # Compute minimum weight matching
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

def create_eulerian_circuit(G, start_node):
    # Ensure all nodes have even degree by adding edges from matching
    eulerian_circuit = list(nx.eulerian_circuit(G, source=start_node))
    return eulerian_circuit

def to_hamiltonian_path(circuit):
    path, visited = [], set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(circuit[0][0])  # append the start node to close the loop
    return path

def calculate_total_cost(path, dist_matrix):
    total_cost = 0
    for i in range(len(path)-1):
        total_cost += dist_matrix[path[i]][path[i+1]]
    return total_cost

# List of city coordinates
cities_positions = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Solve TSP
dist_matrix = create_distance_matrix(cities_positions)
mst = find_minimum_spanning_tree(cities_positions, dist_matrix)

# Create graph from MST
mst_graph = nx.Graph()
mst_graph.add_weighted_edges_from(mst)

# Find odd degree nodes
odd_nodes = [n for n, deg in mst_graph.degree() if deg % 2 == 1]
matching = find_minimum_cost_perfect_matching(odd_nodes, dist_matrix)
mst_graph.add_edges_from(matching)

# Create Eulerian circuit which uses every edge at least once
circuit = create_eulerian_circuit(mst_graph, 0)
hamiltonian_path = to_hamiltonian_path(circuit)
total_cost = calculate_total_cost(hamiltonian_path, dist_matrix)

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)