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

# Step 1: Compute Minimum Spanning Tree (MST)
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = distances[i][j]

mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identifying odd degree vertices
odd_vertices = [x for x in mst.nodes if mst.degree(x) % 2 == 1]

# Step 3: Minimum Weight Perfect Matching on odd degree vertices
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_vertices)
for i in odd_vertices:
    for j in odd_vertices:
        if i != j:
            odd_graph.add_edge(i, j, weight=distances[i][j])

matching = nx.algorithms.matching.min_weight_matching(odd_graph, True)

# Step 4: Combine edges of MST and Matching to form multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Step 5: Find an Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert Eulerian to Hamiltonian by skipping visited nodes
# The purpose is to visit each node exactly once and return to the depot
visited = set()
hamiltonian_circuit = []
total_cost = 0
last = 0

for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
    total_cost += distances[last][v]
    last = v

# Add return path to depot city
hamiltonian_circuit.append(0)
total_cost += distances[last][0]

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")