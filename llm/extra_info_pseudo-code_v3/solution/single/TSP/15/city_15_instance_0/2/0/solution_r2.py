import math
import networkx as nx
from networkx.algorithms import approximation as approx

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(city_positions):
    """ Create a complete graph from a list of city positions. """
    G = nx.Graph()
    for i, pos1 in enumerate(city_positions):
        for j, pos2 in enumerate(city_positions):
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(pos1, pos2))
    return G

def christofides_tsp(city_positions):
    """ Apply Christofides' algorithm to solve the TSP problem. """
    # Step 1: Create a complete graph
    G = create_complete_graph(city_positions)

    # Step 2: Find a Minimum Spanning Tree (MST)
    MST = nx.minimum_spanning_tree(G)

    # Step 3: Find vertices with odd degree in the MST
    odd_degree_nodes = [v for v, degree in MST.degree() if degree % 2 == 1]

    # Step 4: Create subgraph induced by these odd degree vertices
    subgraph = G.subgraph(odd_degree_nodes)

    # Step 5: Find Minimum Weight Perfect Matching (MWPM) on subgraph of odd degree vertices
    MWPM = approx.min_weight_matching(subgraph, maxcardinality=True)

    # Step 6: Combine the MST with the perfect matching to give a multigraph
    multigraph = nx.MultiGraph(MST)
    multigraph.add_edges_from(MWPM)

    # Step 7: Find an Eulerian circuit on the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))

    # Step 8: Convert the Eulerian circuit to Hamiltonian circuit by skipping visited nodes (shortcutting)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # close the circuit back to the start

    # Step 9: Calculate the cost of the tour
    cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

    return path, cost

# Define city positions
city_positions = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Compute the shortest tour using Christofides' algorithm
tour, total_cost = christofides_tsp(city_positions)

# Output the results
print("Tour: ", tour)
print("Total travel cost: %.2f" % total_cost)