import numpy as np
import networkx as nx

# City coordinates
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def create_graph(cities):
    """ Create a complete graph with weighted edges between cities. """
    G = nx.Graph()
    for i, coord1 in enumerate(cities):
        for j, coord2 in enumerate(cities):
            if i != j:
                dist = np.linalg.norm(np.array(coord1) - np.array(coord2))
                G.add_edge(i, j, weight=dist)
    return G

def find_tour(G, start=0):
    """ Find a tour using the 1.5-approximation algorithm based on MST and perfect matching. """
    # Getting the Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(G, weight='weight')

    # Finding odd degree nodes from MST
    odd_degree_nodes = [v for v, deg in mst.degree() if deg % 2 == 1]

    # Create subgraph of G that includes the odd degree nodes
    odd_subgraph = G.subgraph(odd_degree_nodes)

    # Minimum Weight Perfect Matching in the subgraph
    matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

    # Add matching edges to MST
    mst.add_edges_from(matching)

    # Create an Eulerian circuit from the MST + matching
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=start))

    # Convert Eulerian circuit to Hamiltonian path (shortcutting repeated nodes)
    visited = set()
    hamiltonian_circuit = [start]
    for u, v in eulerian_circuit:
        if v not in visited:
            hamiltonian_circuit.append(v)
            visited.add(v)
    hamiltonian_circuit.append(start)  # return to the start

    return hamiltonian_circuit

def calculate_total_cost(G, path):
    """ Calculate total travel cost of the path. """
    return sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

# Create graph and find the tour
G = create_graph(city_coords)
tour = find_tour(G)
total_cost = calculate_total_cost(G, tour)

print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_view_cost))