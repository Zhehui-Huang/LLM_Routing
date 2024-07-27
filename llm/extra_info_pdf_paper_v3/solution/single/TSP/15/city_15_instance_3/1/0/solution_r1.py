import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def euclidean_distance_matrix(coordinates):
    """ Create a distance matrix based on Euclidean distance between points """
    return squareform(pdist(coordinates, metric='euclidean'))

def create_graph(distance_matrix):
    """ Create a graph from the distance matrix """
    G = nx.Graph()
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            if i != j:
                G.add_edge(i, j, weight=distance_matrix[i, j])
    return G

def find_odd_degree_vertices(T):
    """ Find vertices with an odd degree in the given MST """
    return [v for v, degree in T.degree() if degree % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    """ Use the NX algorithm to find the minimum weight perfect matching on specified vertices """
    return nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)

def eulerian_circuit(G, starting_vertex):
    """ Form an Eulerian circuit starting from a specified vertex """
    return list(nx.eulerian_circuit(G, source=starting_vertex))

def hamiltonian_circuit(eulerian_circuit, starting_vertex):
    """ Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices """
    visited = set()
    path = [starting_vertex]  # Start at the starting vertex
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(starting_vertex)  # Return to the starting vertex
    return path

# Define cities' coordinates
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
])

# Create distance matrix and graph
dist_matrix = euclidean_distance_matrix(coordinates)
G = create_graph(dist_matrix)

# Step 1: Create MST using Kruskal's Algorithm
MST = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree in the MST
odd_vertices = find_odd_degree_vertices(MST)

# Step 3: Find minimum-weight perfect matching for the vertices
matching = minimum_weight_perfect_matching(G, odd_vertices)

# Step 4: Combine MST and matching in a multigraph
multi_graph = nx.MultiGraph(MST)
multi_graph.add_edges_from(matching)

# Step 5: Create an Eulerian circuit from the multi graph
euler_circuit = eulerian_circuit(multi_graph, 0)

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
tour = hamiltonian_circuit(euler_circuit, 0)

# Calculate Total Travel Cost
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)