import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree

def main():
    # Define the cities coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Compute the distance matrix
    positions = np.array(list(cities.values()))
    dist_matrix = squareform(pdist(positions, 'euclidean'))

    # Step 1: Compute a minimum spanning tree (MST)
    mst_tree = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i+1, n):
            mst_tree.add_edge(i, j, weight=dist_matrix[i][j])
    mst = nx.minimum_spanning_tree(mst_tree)

    # Step 2: Identify odd degree vertices
    odd_vertices = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

    # Step 3: Minimum-weight perfect matching
    subgraph = mst_tree.subgraph(odd_vertices)
    min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

    # Step 4: Combine edges of MST and matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(min_cost_matching)

    # Step 5: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Step 6: Convert to Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = [0]
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)

    if hamiltonian_circuit[-1] != 0:
        hamiltonian_circuit.append(0)

    # Calculate the total travel cost of the Hamiltonian circuit
    total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

    # Output result
    print("Tour:", hamiltonian_circuit)
    print("Total travel cost:", total_cost)

if __name__ == "__main__":
    main()