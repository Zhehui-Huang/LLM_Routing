import math
import networkx as nx

# Coordinates of the cities
cities = [
    (79, 15),  # Depot city: City 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Helper function to calculate the Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Construct the full graph with cities as nodes and edges weighted by euclidean distances
def construct_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

# Calculates a tour using a TSP heuristic approach
def tsp_heuristic(graph):
    # Step 1: Construct Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(graph)

    # Step 2: Find vertices with odd degree in the MST
    odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

    # Step 3: Minimum Weight Perfect Matching in the subgraph induced by odd degree nodes
    if odd_degree_nodes:
        odd_subgraph = graph.subgraph(odd_degree_nodes)
        matches = nx.algorithms.max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

        # Add these edges to the MST to form a graph that can be made Eulerian
        for u, v in matches:
            mst.add_edge(u, v, weight=graph[u][v]['weight'])

    # Step 4: Form an Eulerian tour
    eulerian_tour = list(nx.eulerian_circuit(nx.eulerize(mst), source=0))

    # Step 5: Convert the Eulerian tour to a single Hamiltonian path
    visited = set()
    path = []
    total_cost = 0
    for u, v in eulerian_tour:
        if u not in visited:
            path.append(u)
            visited.add(u)
        # Calculate cost only when transitioning in the Eulerian tour
        if v not in visited or v == 0:  # Include last trip going back to depot city
            total_cost += graph[u][v]['weight']
    path.append(0)  # Complete the tour by returning to the depot

    return path, total_cost

# Create the graph and calculate solution using the TSP heuristic
graph = construct_graph(cities)
tour, total_travel_cost = tsp_heuristic(graph)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)