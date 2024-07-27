import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

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

# Compute Euclidean distances between each pair of coordinates
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)

def find_odd_degree_vertices(mst):
    rows, cols = mst.nonzero()
    degrees = np.zeros(len(cities), dtype=int)
    for row in rows:
        degrees[row] += 1
    for col in cols:
        degrees[col] += 1
    return np.where(degrees % 2 == 1)[0]

odd_degree_vertices = find_odd_degree_vertices(mst)

# Using a simple greedy algorithm to match odd degree vertices
def greedy_match_odd_vertices(vertices, dist_matrix):
    matches = []
    while vertices:
        v = vertices.pop()
        if vertices:
            distances = [(dist_matrix[v, w], w) for w in vertices]
            _, nearest = min(distances, key=lambda x: x[0])
            vertices.remove(nearest)
            matches.append((v, nearest))
    return matches

matching = greedy_match_odd_vertices(list(odd_degree_vertices), dist_matrix)

# Combine MST and Matching
combined = csr_matrix(mst)
for u, v in matching:
    combined[u, v] = dist_matrix[u, v]
    combined[v, u] = dist_matrix[v, u]

# Find an Eulerian tour
def find_eulerian_tour(graph, start=0):
    tour = []
    num_vertices = graph.shape[0]
    temp_tour = [start]
    while temp_tour:
        u = temp_tour[-1]
        neighbors = graph.indices[graph.indptr[u]:graph.indptr[u+1]]
        if neighbors.size > 0:
            v = neighbors[0]
            temp_tour.append(v)
            graph[u, v] = 0
            graph[v, u] = 0
        else:
            tour.append(temp_tour.pop())
    return tour

tour = find_eulerian_tour(combined)

# Convert Eulerian to Hamiltonian tour
def convert_to_hamiltonian(tour):
    visited = set()
    hamiltonian_tour = []
    for city in tour:
        if city not in visited:
            visited.add(city)
            hamiltonian_tour.append(city)
    return hamiltonian_tour

ham_tour = convert_to_hamiltonian(tour)

# Ensure it starts and ends at the depot
if ham_tour[0] != 0:
    ham_tour = ham_tour[1:] + [ham_tour[0]]
if ham_tour[-1] != 0:
    ham_tour.append(0)

# Calculating the total cost
total_cost = sum(dist_matrix[ham_tour[i], ham_tour[i+1]] for i in range(len(ham_tour) - 1))

print(f"Tour: {ham_tour}")
print(f"Total travel cost: {total_cost:.2f}")