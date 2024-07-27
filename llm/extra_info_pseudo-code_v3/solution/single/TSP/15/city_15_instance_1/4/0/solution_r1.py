import networkx as nx
import math

def main():
    # define city coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }

    # Euclidean distance calculation function
    def euc_dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # Construct the complete graph
    G = nx.Graph()
    for (city1, coords1), (city2, coords2) in combinations(cities.items(), 2):
        # add edge with distance as weight
        distance = euc_dist(coords1, coords2)
        G.add_edge(city1, city2, weight=distance)

    # 1. Compute the Minimum Spanning Tree (MST)
    T = nx.minimum_spanning_tree(G, weight='weight')

    # 2. Find nodes with odd degree
    odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 == 1]
    
    # 3. Minimum weight perfect matching in the subgraph induced by nodes with odd degree
    odd_subgraph = G.subgraph(odd_degree_nodes)
    matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

    # 4. Add matching edges to Tree
    T.add_edges_from(matching)

    # 5. Find Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

    # 6. Create Hamiltonian circuit by skipping repeated nodes
    visited = set()
    hamiltonian_circuit = []
    for u, _ in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
    hamiltonian_circuit.append(0)  # return to the starting point

    # Calculate total cost of the trip
    total_cost = sum(euc_dist(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i+1]]) for i in range(len(hamiltonian_circuit)-1))

    print(f"Tour: {hamiltonian_circuit}")
    print(f"Total travel cost: {total_cost}")

main()