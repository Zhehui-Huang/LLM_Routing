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
    xa, ya = cities[a]
    xb, yb = cities[b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Create a complete graph with cities as nodes and distances as edges
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Implement Christofides algorithm to solve TSP
def christofides_tsp(graph):
    # Step 1: Create a minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Find vertices of odd degree in the MST
    odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]
    
    # Step 3: Find a minimum weight perfect matching among the odd degree nodes
    odd_graph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.max_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    
    # Add the matching edges to the MST
    T.add_edges_from(min_weight_matching)
    
    # Step 4: Create an Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(T, source=0))
    
    # Step 5: Convert the Eulerian circuit to a Hamiltonian path
    path = []
    visited = set()
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # returning to the start point
    return path

# Execute the function and calculate the tour
tour = christofides_tsp(G)

# Calculate the total distance of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print the results: Tour and Total Travel Cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")