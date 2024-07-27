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

# Function to calculate Euclidean distance between two city coordinates
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with cities as nodes
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Christofides algorithm to find a near-optimal solution to the TSP
def christofides_tsp(G, starting_node=0):
    # Step 1: Create a minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(G, weight='weight')

    # Step 2: Find vertices with odd degree in MST
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

    # Step 3: Minimum weight perfect matching on the subgraph induced by odd-degree vertices
    min_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    mst.add_edges_from(min_matching)

    # Step 4: Create Eulerian circuit from the graph
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=starting_node))

    # Step 5: Convert Eulerian circuit to Hamiltonian path, removing repeated nodes
    path, visited = [starting_node], set([starting_node])
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(starting_node) # go back to the starting node

    # Calculate total distance of the tour
    total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
    
    return path, total_cost

# Execute the algorithm
tour_path, total_travel_cost = christofides_tsp(G)

# Output the results
print("Tour:", tour_path)
print("Total travel cost:", round(total_travel_cost, 2))