import math
import networkx as nx

# City coordinates
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

# Calculate Euclidean distances
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

n = len(cities)
distances = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create complete graph with weighted edges (Euclidean distances)
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=distances[i][j])

# Step 1: Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identifying vertices with an odd degree
odd_vertices = [x for x in mst.nodes if mst.degree(x) % 2 == 1]

# Step 3: Construct subgraph with odd degree vertices
odd_graph = G.subgraph(odd_subgraph)

# Finding the minimum weight perfect matching in the subgraph of odd degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of MST and Matching to form the multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Step 5: Create the Eulerian circuit from the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Hamiltonian circuit is an Eulerian circuit without repeating nodes
visited = set()
hamiltonian_circuit = []
last = 0
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_cost += distances[last][v]
        last = v

# Complete the tour to the starting point
hamiltonian_circuit.append(0)
total_cost += distances[last][0]

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")