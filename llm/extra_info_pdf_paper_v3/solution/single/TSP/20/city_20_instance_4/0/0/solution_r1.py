import math
import networkx as nx

# Step 1: Define city coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
          (64, 72), (14, 89)]

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 2: Calculate Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find all vertices with odd degree to perform matching
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 4: Find minimum weight perfect matching
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')

# Add the matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 5: Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
last_city = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        if v != 0:  # to prevent adding the starting node twice at the beginning
            hamiltonian_circuit.append(v)
        if v in visited:
            continue  # Skip adding the cost if it's returning to the depot prematurely
        total_cost += G[last_city][v]['weight']
        visited.add(v)
        last_city = v

# Return to depot city from the last city
hamiltonian_circuit.append(0)
total_cost += G[last_city][0]['weight']

# Output result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")