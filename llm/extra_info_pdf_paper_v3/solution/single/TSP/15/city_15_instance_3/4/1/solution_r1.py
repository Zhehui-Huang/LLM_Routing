import math
import networkx as nx

# Define the city coordinates including the depot city
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 6: (6, 61),
    7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 12: (70, 95),
    13: (29, 64), 14: (32, 79)
}

# Function to compute Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create a complete graph with nodes as cities and edges as distances
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Christofides algorithm implementation to solve TSP
def christofides_tsp(graph):
    # Step 1: Create a minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Find vertices with odd degree in MST
    odd_degree_nodes = [v for v, degree in T.degree if degree % 2 == 1]
    
    # Step 3: Minimum Weight Perfect Matching on the subgraph of odd-degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Add the matching edges to the MST
    T.add_edges_from(matching)
    
    # Step 4: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(T)))
    
    # Convert Eulerian circuit to a Hamiltonian path: avoid repeated nodes
    visited = set()
    path = [eulerian_circuit[0][0]]
    visited.add(eulerian_circuit[0][0])
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    
    # Add start city to end to complete the tour
    path.append(path[0])
    return path

# Calculate the shortest tour and the total travel cost
tour = christofides_tsp(G)
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print the Tour and Total Travel Cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")