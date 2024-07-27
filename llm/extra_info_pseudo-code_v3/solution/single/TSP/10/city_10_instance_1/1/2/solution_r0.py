import math
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities
n = len(cities)

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate the graph's weight matrix
weights = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            weights[i][j] = euclidean_distance(cities[i], cities[j])

# Step 1: Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(weights)).toarray()

# Step 2: Identify vertices of odd degree in MST
degree = [0] * n
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            degree[i] += 1
            degree[j] += 1

odd_vertices = [idx for idx, deg in enumerate(degree) if deg % 2 != 0]

# Step 3: Minimum weight perfect matching on odd degree vertices
def minimum_weight_matching(odd_vertices, weights):
    num_vertices = len(odd_vertices)
    graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            v1, v2 = odd_vertices[i], odd_vertices[j]
            graph.add_edge(v1, v2, weight=weights[v1][v2])

    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return matching

matching = minimum_weight_matching(odd_vertices, weights)

# Step 4: Create multigraph H adding edges from MST and matching
multi_graph = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            multi_graph.add_edge(i, j, weight=mst[i][j])

for edge in matching:
    multi_graph.add_edge(*edge, weight=weights[edge[0]][edge[1]])

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited and v != 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(weights[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)