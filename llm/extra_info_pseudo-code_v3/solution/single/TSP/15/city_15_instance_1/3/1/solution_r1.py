import math
import networkx as nx

def euclidean_distance(p1, p2):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_graph(cities):
    """ Create a complete graph from city coordinates """
    G = nx.Graph()
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def christofides_algorithm(G):
    """ Implement Christofides algorithm to find TSP solution """
    # Step 1: Compute a minimum spanning tree (MST) of G
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Identify the set O of vertices with odd degree in T
    odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 != 0]
    
    # Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    
    # Step 4: Add the matching edges to T
    T.add_edges_from(min_weight_matching)
    
    # Step 5: Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))
    
    # Step 6: Convert Eulerian circuit to Hamiltonian path by skipping visited nodes
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the start point
    
    return path

# Coordinates of the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Create the graph from the cities
G = create_graph(cities)

# Apply Christofides algorithm to find a solution
tour = christofides_algorithm(G)

# Calculate the total travel cost
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")