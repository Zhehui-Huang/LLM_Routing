import math
import networkx as nx

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Construct graph
G = nx.Graph()
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Create MST using Kruskal's Algorithm
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Find vertices with an odd degree in the MST
odd_vertices = [v for v, degree in mst.degree() if degree % 2 != 0]

# Create complete graph on the vertices with odd degree
odd_vertex_subgraph = nx.complete_graph(odd_vertices)
for i, j in odd_vertex_subgraph.edges():
    odd_vertex_subgraph[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Find minimum weight perfect matching (max weight matching with negated weights for min matching)
min_matching = nx.algorithms.matching.min_weight_matching(odd_vertex_subgraph, maxcardinality=True)

# Add matching edges to the MST
mst.add_edges_from(min_matching)

# Create Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_path = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)

# Ensure the starting city is the same as the ending city
hamiltonian_path.append(0)

# Calculate the total travel cost
total_cost = sum(euclidean_distance(cities[hamiltonian_path[i]], cities[hamiltonian_path[i+1]]) for i in range(len(hamiltonian_path)-1))

# Output the results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)