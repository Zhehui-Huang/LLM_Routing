import math
import networkx as nx

# Define the coordinates of each city
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate the Euclidean distances between each pair of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate the complete graph of cities with distance as weight
def generate_complete_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Christofides algorithm to find a tour
def christofides_algorithm(G):
    # Step 1: Create a Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Find vertices with odd degree in the MST
    odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]
    
    # Step 3: Find minimum weight perfect matching among odd degree vertices in MST
    odd_graph = nx.Graph(mst.subgraph(odd_degree_nodes))
    for u, v in odd_graph.edges():
        odd_graph[u][v]['weight'] = G[u][v]['weight']
    min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

    # Add the minimum weight matching edges to the MST
    mst.add_edges_from(min_weight_matching)

    # Step 4: Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

    # Step 5: Make the circuit a Hamiltonian path (remove repeated vertices)
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            path.append(v)
    path.append(path[0])  # Complete the tour by returning to the start
    
    return path

# Main execution
G = generate_complete_graph(cities)
tour = christofides_algorithm(G)

# Calculate the total distance of the tour
total_distance = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Display results
print("Tour:", tour)
print("Total travel cost:", total_distance)