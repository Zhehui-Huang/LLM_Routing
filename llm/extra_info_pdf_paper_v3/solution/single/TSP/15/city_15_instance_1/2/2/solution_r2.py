import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def tsp_heuristic(cities):
    G = create_graph(cities)
    mst = nx.minimum_spanning_tree(G)  # Compute the MST
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 != 0]
    subgraph = G.subgraph(odd_degree_nodes)
    match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    
    augmented_mst = mst.copy()
    augmented_mst.add_edges_from(match)
    
    # Make the graph Eulerian by duplicating edges
    eulerian_graph = nx.eulerize(augmented_mst)
    eulerian_tour = list(nx.eulerian_circuit(eulerian_graph, source=0))
    
    # Convert Eulerian circuit to Hamiltonian path
    visited = set()
    path = [0]
    travel_cost = 0
    for (u, v) in eulerian_tour:
        if v not in visited:
            travel_cost += G[u][v]['weight']
            path.append(v)
            visited.add(v)
    # Closing the loop
    travel_cost += G[path[-1]][0]['weight']
    path.append(0)
    
    return path, travel._cost

# Define the cities' coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Solve the TSP
tour, total_cost = tsp_heuristic(cities)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)