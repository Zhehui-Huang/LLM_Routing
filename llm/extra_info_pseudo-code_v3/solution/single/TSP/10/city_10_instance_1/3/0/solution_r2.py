import math
import networkx as nx

# Define coordinates for each city including depot
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct a complete graph with cities as nodes
def create_complete_graph(coordinates):
    G = nx.Graph()
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))
    return G

# Step-by-step implementation of Christofides' algorithm
def christofides_algorithm(coordinates):
    G = create_complete_graph(coordinates)
    
    # Step 1: Compute a minimum spanning tree
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Identify vertices of odd degree
    O = [v for v in T.nodes() if T.degree(v) % 2 == 1]
    
    # Step 3: Minimum-weight perfect matching on vertices with odd degree
    subgraph_O = G.subgraph(O)
    M = nx.algorithms.matching.min_weight_matching(subgraph_O, maxcardinality=True)
    
    # Step 4: Combine the edges of T and M
    H = nx.MultiGraph(T)
    H.add_edges_from(M)
    
    # Step 5: Find Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Convert Eulerian to Hamiltonian circuit
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Completing the circuit by returning to the start
    
    # Calculate total cost
    total_cost = sum(euclidean_distance(coordinates[path[i]], coordinates[path[i+1]]) for i in range(len(path) - 1))
    
    return path, total_cost

# Execute the algorithm
tour, total_cost = christofides_algorithm(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)