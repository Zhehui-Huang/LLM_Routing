import math
import networkx as nx

# City coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()

# Add nodes and edges with weights
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Function to find a minimum cost perfect matching
def min_cost_perfect_matching(G, nodes):
    subgraph = G.subgraph(nodes)
    return nx.algorithms.matching.min_weight_matching(subgraph, True, weight="weight")

# Christofides algorithm to generate approximate solution
def christofides_tsp(G, starting_node=0):
    # Step 1: Create a minimum spanning tree
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Step 2: Find nodes with odd degree
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Find minimum cost perfect matching in the induced subgraph
    min_matching = min_cost_perfect_matching(G, odd_degree_nodes)
    T.add_edges_from(min_matching)
    
    # Step 4: Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T, source=starting_node))
    
    # Step 5: Make the circuit a Hamiltonian circuit by skipping visited nodes (shortcutting)
    visited = set()
    path = [starting_node]
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    
    path.append(starting_node)  # Adding the start point to complete the circuit
    
    # Calculate the total cost of the tour
    total_cost = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
    
    return path, total_rbdsa