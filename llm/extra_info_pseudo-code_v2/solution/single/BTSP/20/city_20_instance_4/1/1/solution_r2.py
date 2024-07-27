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

def euclidean_distance(c1, c2):
    """Euclidean distance between two city coordinates"""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Construct a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Heuristic function to find an approximate solution for Bottleneck Traveling Salesman Problem (BTSP)
def find_btsp_tour(graph):
    # Step 1: Construct a minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(graph)
    
    # Step 1b: Make it biconnected (by duplicating edges - simple approach for a demo)
    mst_bi = nx.MultiGraph(mst)
    mst_bi.add_edges_from(mst.edges())
    
    # Step 2: Find an Eulerian circuit in the created multigraph, which visits each edge exactly once
    euler_circuit = list(nx.eulerian_circuit(mst_bi, source=0))
    
    # Step 3: Create a Hamiltonian circuit by skipping repeated nodes (shortcutting)
    path = [0]  # start at the depot
    visited = set([0])
    for u, v in euler_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(0)  # end at the depot

    # Calculate max edge weight and total tour cost
    max_edge_weight = max(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
    total_cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
    
    return path, total_cost, max_edge_weight

# Calculate the tour, total cost, and maximum distance between any two consecutive cities
tour, total_cost, max_distance = find_btsp_tour(G)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")