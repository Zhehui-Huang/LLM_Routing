import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import tree, matching 

def compute_euclidean_distance_matrix(coordinates):
    return distance_matrix(coordinates, coordinates)

def get_minimum_spanning_tree(coords):
    G = nx.complete_graph(len(coords))
    for i in range(len(coords)):
        for j in range(len(coords)):
            G[i][j]['weight'] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    MST = tree.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    return MST

def get_odd_degree_vertices(MST):
    return [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

def find_minimum_weight_perfect_matching(G, odd_degree_vertices):
    subgraph = G.subgraph(odd_degree_vertices)
    return matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def find_eulerian_circuit(multigraph, start_node):
    return list(nx.eulerian_circuit(nx.MultiGraph(multigraph), source=start_node))

def create_tour(eulerian_circuit):
    tour = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0])  # to complete the cycle
    return tour

def calculate_total_cost(G, tour):
    cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
    return cost

coords = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(len(coords)):
        if i != j:
            G[i][j]['weight'] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))

MST = get_minimum_spanning_tree(coords)
odd_degree_vertices = get_odd_degree_vertices(MST)
matching_edges = find_minimum_weight_perfect_matching(G, odd_degree_vertices)

MST.add_edges_from(matching_edges)
eulerian_circuit = find_eulerian_circuit(MST, start_node=0)
tour = create_tour(eulerian_circuit)
total_cost = calculate_total_cost(G, tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")