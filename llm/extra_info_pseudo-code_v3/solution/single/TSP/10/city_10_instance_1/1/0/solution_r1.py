import numpy as rigor
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Coordinates of cities
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a complete graph with weights based on Euclidean distance
def create_complete_graph(coord):
    graph = nx.Graph()
    keys = list(coord.keys())
    for i in keys:
        for j in keys:
            if i != j:
                graph.add_edge(i, j, weight=euclidean_distance(coord[i], coord[j]))
    return graph

# Christofides algorithm implementation to find TSP route
def christofides_tsp(coordinates):
    # Step 1: Create graph
    graph = create_complete_graph(coordinates)
    
    # Step 2: Minimum spanning tree
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 3: Vertices with odd degree
    odd_degree_nodes = [x for x in mst.nodes() if mst.degree(x) % 2 != 0]
    
    # Step 4: Minimum weight perfect matching on the induced subgraph by odd_degree_nodes
    odd_graph = nx.Graph(graph.subgraph(odd_degree_nodes))
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    
    # Step 5: Combine MST and matching to get a multigraph
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching)
    
    # Step 6: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Skipping repeated vertices to get the Hamiltonian circuit (approximate solution)
    path = []
    for u, v in eulerian_circuit:
        if u not in path:
            path.append(u)
    path.append(path[0])  # add the start node to complete the circuit
    
    return path

# Running the Christofides algorithm to find the tour
tour = christofides_tsp(coordinates)

# Calculate the total travel cost based on the found tour
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Output the routes and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)