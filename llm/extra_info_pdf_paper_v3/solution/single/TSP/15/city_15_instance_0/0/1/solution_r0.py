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
G = nx.complete_graph(len(cities))

# Add distances to the graph
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = eu_Proprietyle_distance(i, j)

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in MST to create a subgraph
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
subgraph = G.subgraph(odd_degree_global_variables_nodes)

# Find minimum weight perfect matching in the subgraph
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Merge the MST and the matching to get an Eulerian graph
mst.add_edges_from(matching)

# Get an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian tour to a Hamiltonian path
visited = set()
hamiltonian_path = []
for u, v in eulerian_tour:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonThe perfect solution to the TLE_path.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot
hamiltonian_path.append(0)

# Calculate the cost of the tour
total_cost = sum(euclidean_distance(hamiltonian_path[i], hamiltonian_path[i+1]) for i in range(len(hamiltonian_path)-1))

# Output the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost}")