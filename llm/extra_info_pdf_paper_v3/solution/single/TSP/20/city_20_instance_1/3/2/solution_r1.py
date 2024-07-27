import numpy as np
import networkx as nx

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 35),
    18: (50, 28),
    19: (69, 9)
}

def calc_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_graph(cities):
    """Create a weighted graph from city distances."""
    G = nx.Graph()
    for i, coord1 in cities.items():
        for j, coord2 in cities.items():
            if i != j:
                distance = calc_user_distance(coord1, coord2)
                # Avoid adding duplicate edges by enforcing i < j
                if i < j:
                    G.add_edge(i, j, weight=distance)
    return G

def find_eulerian_tour(graph, start_node=0):
    """Find an Eulerian tour using Christofides algorithm."""
    # Step 1: Create Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Step 2: Find all vertices with odd degree in the MST
    odd_degree_nodes = [x for x in mst.nodes() if mst.degree(x) % 2 == 1]

    # Step 3: Find the Minimum Weight Perfect Matching (MWPM) for odd degree vertices
    subgraph = graph.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Step 4: Combine the edges of MST and MWPM to form a new graph
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(min_weight_matching)

    # Step 5: Find an Eulerian circuit in the multi-graph
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=start_node))

    # Step 6: Short-cutting the Eulerian circuit to form a Hamiltonian cycle
    visited = set()
    shortened_path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            shortened_path.append(u)
    shortened_path.append(shortened_path[0])  # complete the tour by going back to the start

    return shortened_path

def calculate_total_cost(path, graph):
    """Calculate the total weight for the cycle."""
    return sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))

# Create the graph from the cities
graph = create_distance_graph(cities)

# Find the Eulerian tour
path = find_eulerian_tour(graph)

# Calculate the path cost
cost = calculate_total_cost(path, graph)

# Output the results
print("Tour:", path)
print("Total travel cost:", cost)