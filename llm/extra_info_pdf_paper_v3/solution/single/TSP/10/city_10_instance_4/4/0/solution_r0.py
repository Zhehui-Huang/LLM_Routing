import networkx as nx
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree
odd_degree_nodes = [v for v in mst.nodes if mst.degree[v] % 2 == 1]

# Create subgraph of nodes with odd degree
odd_graph = G.subgraph(odd_degree_nodes)

# Find minimum cost perfect matching
matches = nx.algorithms.max_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add edges from matching to the MST
mst.add_edges_from(matches)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to a Hamiltonian path - remove repeated nodes
visited = set()
path = []
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
    if v not in visited:
        path.append(v)
        visited.add(v)

# Ensure the tour returns to the starting depot
path.append(path[0])

# Calculate total travel cost of the path
total_travel_cost = 0
for i in range(len(path) - 1):
    total_travel_cost += distance(cities[path[i]], cities[path[i + 1]])

# Output
print("Tour:", path)
print("Total travel cost:", total_travel_cost)