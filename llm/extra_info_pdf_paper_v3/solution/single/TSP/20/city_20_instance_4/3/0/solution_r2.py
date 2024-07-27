import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, is_eulerian, eulerian_circuit

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates indexed by city number
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Create matrix of distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(20)] for i in range(20)]

# Create a graph instance to use with networkx
G = Graph()
for i in range(20):
    for j in range(i + 1, 20):
        G.add_edge(i, j, weight=distances[i][j])

# Obtain the Minimum Spanning Tree (MST)
T = Graph(minimum_spanning_tree(G))

# Find all vertices of odd degree in the MST
odd_vertices = [v for v in T if T.degree(v) % 2 != 0]

# Perform the minimum weight perfect matching on the odd degree vertices to get augmented graph H
min_weight_matches = nx.algorithms.max_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)

# Add these edges to T
T.add_edges_from(min_weight_matches)

# Ensure the graph has an Eulerian circuit (all vertices even degree) and find Eulerian circuit
assert is_eulerian(T)
eulerian_path = list(eulerian_circuit(T, source=0))

# Convert Eulerian circuit to Hamiltonian Path (shortcutting)
visited = set()
tour = [0]
total_cost = 0
current = 0

for u, v in eulerian_path:
    if v not in visited or v == 0:  # to allow return to the starting node
        if v == 0 and len(visited) < 19:
            continue
        tour.append(v)
        total_cost += distances[current][v]
        visited.add(v)
        current = v

# Ensure the tour is valid by checking all cities are visited once
assert len(tour) == 21  # including the return to the depot

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")