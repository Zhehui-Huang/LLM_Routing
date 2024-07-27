import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

def main():
    # Define the cities coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
        6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
        12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # Calculate the Euclidean distance matrix
    coords = np.array(list(cities.values()))
    dist_matrix = distance_matrix(coords, coords)

    # Create a complete graph
    G = nx.complete_graph(len(cities))
    for i, j in combinations(G.nodes, 2):
        G[i][j]['weight'] = dist_matrix[i][j]

    # Compute a minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(G, weight='weight')

    # Find vertices with odd degree
    O = [v for v, d in T.degree() if d % 2 == 1]

    # Minimum Weight Perfect Matching on the odd degree vertices
    odd_subgraph = G.subgraph(O)
    matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

    # Add the matching edges to T
    T.add_edges_from(matching)

    # Compute an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

    # Convert Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
    hamiltonian_circuit = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # return to the starting point

    # Compute the total travel cost
    total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

    # Output the results
    print("Tour:", hamiltonian_circuit)
    print("Total travel cost:", total_cost)

if __name__ == "__main__":
    main()