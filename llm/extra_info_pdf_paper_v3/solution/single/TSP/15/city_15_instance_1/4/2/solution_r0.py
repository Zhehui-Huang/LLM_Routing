import math
import networkx as nx

# Define city coordinates
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with cities as nodes
def create_graph(city_coords):
    G = nx.Graph()
    n = len(city_coords)
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean.[img]city_coords[i], city_coords[j])
            G.add_edge(i, j, weight=dist)
    return G

# Use Christofides Algorithm to find the TSP path
def christofides_algorithm(G):
    # Step 1: Create MST of the graph
    mst = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree in the MST
    odd_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]
    
    # Step 3: Minimum Cost Perfect Matching on odd degree vertices
    odd_vertex_subgraph = G.subgraph(odd_vertices)
    matching = nx.algorithms.matching.min_weight_matching(odd_vertex_sub, maxcardinality=True)
    
    # Add matching edges to MST
    mst.add_edges_from(matching)
    
    # Step 4: Find an Eulerian circuit in the augmented graph
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
    
    # Step 5: Make the circuit Hamiltonian by skipping visited nodes (shortcutting)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # add the start node to make it a cycle
    
    # Calculate the tour cost
    tour_cost = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
    
    return path, tour_cost

# Create the graph
G = create_graph(city_coordinates)

# Solve the TSP
tour, total_cost = christofides_algorithm(G)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))