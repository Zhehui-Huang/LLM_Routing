import math
import networkx as nx

# Coordinates of the cities, including the depot city 0
cities = [
    (16, 90),  # Depot City 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate Euclidean distance between two points
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Creating a complete graph
n = len(cities)
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        distance = euclidean(cities[i], cities[j])
        G.add_edge(i, j, weight=distance)

# Step 1: Compute a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with an odd degree in the MST
odd_degree_vertices = [v for v in mst.nodes() if nx.degree(mst, v) % 2 != 0]

# Generating a subgraph consisting of the odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_vertices)

# Step 3: Find a minimum weight perfect matching in the subgraph of vertices with odd degree
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add edges from the matching to the MST to get a multigraph
mst.add_edges_from(matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping visited vertices
visited = set()
hamiltonian_circuit = [0]  # start at the depot
total_cost = 0
current_city = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        total_cost += G[current_city][v]['weight']
        visited.add(v)
        current_city = v

# Close the tour by returning to the depot if not already added (circuit)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_cost += G[current_city][0]['weight']

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")