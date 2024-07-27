import math
import networkx as nx

# City coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating a complete graph
def create_complete_graph():
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Christofides Algorithm
def christofides_algorithm():
    # Step 1: Create a complete graph
    G = create_complete_google_graph()
    
    # Step 2: Compute Minimum Spanning Tree (MST)
    MST = nx.minimum_spanning_tree(G)

    # Step 3: Find vertices with odd degree
    odd_degree_nodes = [v for v, d in MST.degree() if d % 2 == 1]

    # Step 4: Minimum Weight Perfect Matching (MWPM)
    # Create subgraph with odd degree vertices
    odd_subgraph = G.subgraph(odd_degree_nodes)
    mwpm = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight="weight")

    # Step 5: Merge the MST and the MWPM
    multigraph = nx.MultiGraph(MST)
    for edge in mwpm:
        multigraph.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]["weight"])

    # Step 6: Find an Eulerian circuit on the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))

    # Step 7: Make Hamiltonian circuit (remove duplicates)
    hamiltonian_circuit = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # complete the circuit back to the depot city

    # Calculate total cost of the Hamiltonian circuit
    total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]["weight"] for i in range(len(hamiltonian_circuit) - 1))

    return hamiltonian_circuit, total_cost

# Compute the tour using Christofides algorithm
tour, total_cost = christofides_algorithm()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)