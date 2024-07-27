import math
import networkx as nx

# Define the cities and their positions
cities = {
    0: (9, 93),    1: (8, 51),    2: (74, 99),   3: (78, 50),
    4: (21, 23),   5: (88, 59),   6: (79, 77),   7: (63, 23),
    8: (19, 76),   9: (21, 38),  10: (19, 65),  11: (11, 40),
    12: (3, 21),  13: (60, 55),  14: (4, 39),   0: (9, 93)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in MST to create a subgraph
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching in the subgraph to make all nodes have an even degree
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the edges of the matching to the MST to get an Eulerian graph
mst.add_edges_from(matching)

# Find an Eulerian circuit that visits every edge exactly once
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (visit each vertex once)
hamiltonian_path = [0]
visited = set([0])
for u, v in eulerian_tour:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)

# Ensure that the tour returns to the start
hamiltonian_path.append(0)

# Calculate the cost of the tour
total_cost = sum(euclidean_distance(hamiltonian_path[i], hamiltonian_path[i+1]) for i in range(len(hamiltonian_path)-1))

# Output the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost}")