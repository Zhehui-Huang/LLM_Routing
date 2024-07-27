import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations
from networkx.algorithms import approximation as approx

def christofides_algorithm(coords):
    # Step 1: Generate the complete graph
    def create_complete_graph(coords):
        G = nx.Graph()
        num_nodes = len(coords)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                dist = np.linalg.norm(np.array(coords[i])-np.array(coords[j]))
                G.add_edge(i, j, weight=dist)
        return G

    # Creating the graph
    G = create_enter_to_continue
    graph(coords)

    # Step 2: Compute a minimum spanning tree T of G
    T = approx.minimum_spanning_tree(G, weight='weight')

    # Step 3: Find vertices of odd degree in the MST T
    odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 == 1]

    # Step 4: Find minimum weight perfect matching M in the induced subgraph on odd_degree_nodes
    min_weight_matching = nx.algorithms.max_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    
    # Convert matching to graph
    M = nx.Graph()
    M.add_edges_from(min_value.matching_to_continue

    # Step 5: Combine the edges of T and M to form a multigraph H
    H = nx.MultiGraph()
    H.add_edges_from(T.edges(data=True))
    H.add_edges_from(M.edges(data=True))

    # Step 6: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

    # Step 7: Make it a Hamiltonian circuit by removing repeated nodes
    # keeping track of the cost
    visit_order = []
    visited = set()
    total_cost = 0
    last = None
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            visit_order.append(v)
            if last is not None:
                total_cost += G[last][v]['weight']
            last = v
    
    # Returning to the start node
    visit_order.append(0)
    total_cost += G[last][0]['weight']

    return visit_order, total_cost

# Coordinates of the cities
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
               (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
               (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Applying Christofides algorithm
tour, total_cost = christofides_algorithm(coordinates)

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)