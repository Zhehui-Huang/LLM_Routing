import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

def calculate_euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

def create_graph(cities):
    G = nx.Graph()
    num_cities = len(cities)
    G.add_nodes_from(range(num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=calculate_euclidean_distance(cities[i], cities[j]))
    return G

def find_odd_degree_vertices(G):
    return [v for v, d in G.degree() if d % 2 != 0]

def min_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return min_weight_match

def create_eulerian_circuit(G, starting_node=0):
    return list(nx.eulerian_circuit(G, source=starting_node))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the starting point
    return path

def calculate_total_cost(G, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += G[path[i]][path[i + 1]]['weight']
    return cost

# City coordinates
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Step 1: Create the graph
G = create_graph(city_coords)

# Step 2: Compute MST
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find odd degree vertices
odd_degree_vertices = find_odd_degree_vertices(mst)

# Step 4: Find minimum cost perfect matching of odd degree vertices
matching = min_weight_perfect_matching(G, odd_degree_vertices)

# Step 5: Add matching to MST to create an Eulerian graph
mst.add_edges_from(matching)

# Step 6: Create an Eulerian circuit
eulerian_circuit = create_eulerian_circuit(mst)

# Step 7: Create Hamiltonian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Step 8: Calculate total travel cost
total_cost = calculate_total_cost(G, hamiltonian_circuit)

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")