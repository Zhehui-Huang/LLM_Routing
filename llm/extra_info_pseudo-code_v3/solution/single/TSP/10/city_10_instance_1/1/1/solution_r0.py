import math
import networkx as nx
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def christofides_algorithm(cities):
    G = nx.Graph()
    num_cities = len(cities)

    # Creating complete graph
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    
    # Step 1: Compute the minimum spanning tree
    T = nx.minimum_spanning_tree(G)

    # Step 2: Find vertices with an odd degree
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

    # Step 3: Find minimum weight perfect matching
    # Create subgraph containing nodes with an odd degree
    M = nx.Graph()
    M.add_nodes_from(odd_degree practicalitions)
    for pair in combinations(odd_degree_nodes, 2):
        M.add_edge(pair[0], pair[1], weight=G[pair[0]][pair[1]]['weight'])

    min_matching = nx.algorithms.matching.min_weight_matching(M, True)

    # Step 4: Combine edges of T and M to form multigraph H
    H = nx.MultiGraph(T)
    for edge in min_matching:
        H.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['_weight'])

    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

    # Step 6: Convert to Hamiltonian circuit by skipping repeats
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
    
    hamiltonian_circuit.append(0)  # to return to the start city

    # Calculate the total tour cost
    total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

    return hamiltonian_circuit, total_cost

# Define the city coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Find the tour and cost
tour, cost = christofides_algorithm(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")