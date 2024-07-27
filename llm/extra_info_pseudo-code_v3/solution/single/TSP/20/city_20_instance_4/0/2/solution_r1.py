import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_complete_graph(coords):
    G = nx.Graph()
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            G.add_edge(i, j, weight=calculate_distance(coords[i], coords[j]))
    return G

def minimum_weight_perfect_matching(G, vertices):
    min_weight_match = nx.Graph()
    while vertices:
        v = vertices.pop()
        min_weight = float('inf')
        closest_u = None
        for u in vertices:
            weight = G[v][u]['weight']
            if weight < min_weight:
                min_weight = weight
                closest_u = u
        min_weight_match.add_edge(v, closest_u, weight=min_weight)
        vertices.remove(closest_u)
    return min_weight_match

def create_hamiltonian_circuit(circuit, start_node):
    path = [start_node]
    visited = set(path)
    cost = 0
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            cost += G[u][v]['weight']
            visited.add(v)
    # Close the tour
    path.append(start_node)
    cost += G[path[-1]][start_node]['weight']
    return path, cost

# Coordinates of the cities
coords = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Step 1: Create the complete graph G
G = create_complete_graph(coords)

# Step 2: Compute the minimum spanning tree (MST) T
T = find_mst(G)

# Step 3: Identify the set O of odd degree vertices in T
O = find_odd_degree_vertices(T)

# Step 4: Find the minimum weight perfect matching M in the subgraph induced by O
M = minimum_weight_perfect_matching(G, O)

# Step 5: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in multigraph H
circuit = eulerian_circuit(H)

# Step 7: Convert the Eulerian circuit to Hamiltonian circuit
tour, total_cost = create_hamiltonian_circuit(circuit, 0)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)