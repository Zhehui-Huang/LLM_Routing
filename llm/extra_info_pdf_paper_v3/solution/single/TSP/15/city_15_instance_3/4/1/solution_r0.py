import math
import networkx as nx

# Cities coordinates including the depot city
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 6: (6, 61),
    7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 12: (70, 95),
    13: (29, 64), 14: (32, 79)
}

# Function to compute the Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create a complete graph with cities as nodes and distances as edges
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Apply the 1.5-approximation Christofides algorithm to the graph
def christofides_tsp(graph):
    # Step 1: Create a minimum spanning tree
    T = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Find vertices of odd degree
    odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]
    
    # Step 3: Create sub-graph from nodes with odd degrees
    sub_graph = graph.subgraph(odd_degree_nodes)
    
    # Step 4: Find minimum cost perfect matching to create an Eulerian circuit
    matching_graph = nx.algorithms.max_weight_matching(sub_graph, maxcardinality=True, weight='weight')
    T.add_edges_from(matching_graph)
    
    # Step 5: Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T))
    
    # Step 6: Convert to Hamiltonian circuit (shortest tour)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    
    # Ensure the robot returns to the starting point
    if path[0] != path[-1]:
        path.append(path[0])
    
    return path

# Compute the shortest tour using the Christofides algorithm
tour = christofides_tsp(G)

# Compute the total travel cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")