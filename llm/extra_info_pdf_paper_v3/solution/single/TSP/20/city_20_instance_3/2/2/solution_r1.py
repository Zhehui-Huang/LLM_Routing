import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities coordinates
cities = [
    (30, 56),
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Calculate distance matrix
n = len(cities)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Create the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))
mst = mst.toarray().astype(float)

# Find vertices with odd degree in MST
odd_degree_vertices = []
for i in range(n):
    if sum(1 for j in range(n) if mst[i][j] > 0) % 2 != 0:
        odd_degree_vertices.append(i)

# Find minimum cost perfect matching for odd degree vertices
min_cost_match = float('inf')
best_matching = None
for matching in combinations(odd_degree_vertices, len(odd_degree_vertices)//2):
    current_cost = sum(dist_matrix[u][v] for u, v in zip(matching, odd_degree_vertices if u != v))
    if current_cost < min_cost_match:
        min_cost_match = current_cost
        best_matching = matching

# Add edges from the best matching to the MST
for u, v in best_matching:
    mst[u][v] = dist_matrix[u][v]
    mst[v][u] = dist_matrix[v][u]

# Create an Eulerian circuit (which in this case, serves as an Hamiltonian circuit)
# We need to double the matched edges and find an Eulerian trail
def eulerian_tour(graph, start_vertex):
    path = []
    stack = [start_vertex]
    while stack:
        current = stack[-1]
        available_edges = [j for j in range(n) if graph[current][j] != float('inf')]
        if not available_edges:
            path.append(stack.pop())
        else:
            next_vertex = available_edges[0]
            graph[current][next_vertex] = graph[next_vertex][current] = float('inf')
            stack.append(next_vertex)
    return path

tour = eulerian_tour(mst, 0)

# Calculate the total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output required format
print("Tour:", tour + [tour[0]])
print("Total travel cost:", total_cost)