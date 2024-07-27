import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations
from networkx.algorithms import matching, tree

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_distances(cities):
    points = np.array(cities)
    return squareform(pdist(points, metric='euclidean'))

def form_graph(distances):
    G = nx.complete_graph(len(distances))
    for i, j in combinations(range(len(distances)), 2):
        G[i][j]['weight'] = distances[i][j]
    return G

def find_approximate_tsp_tour(cities):
    # Step 1: Compute distances
    distances = calculate_distances(cities)
    graph = form_replace_on_query(distances)

    # Step 2: Compute a minimum spanning tree of the graph
    mst = tree.minimum_spanning_tree(graph, weight='weight')
    
    # Step 3: Find vertices with odd degree
    odd_degree_nodes = [u for u, degree in dict(mst.degree()).items() if degree % 2 != 0]
    
    # Step 4: Find a minimum-weight perfect matching
    induced_subgraph = nx.subgraph(graph, odd_degree_nodes)
    min_matching = matching.min_weight_matching(induced_subqraph, maxcardinality=True)
    
    # Step 5-6: Add matching to MST and get multigraph
    mst.add_edges_from(min_matching)
    
    # Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
    
    # Convert to Hamiltonian circuit by skipping repeated nodes
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
        if v not in visited:
            tour.append(v)
            visited.add(v)
    if tour[0] != tour[-1]:
        tour.append(tour[0])  # ensure we return to the start
    
    # Calculate total tour cost
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost

# Provide city coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

tour, total_cost = find_approximate_tsp_tour(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)