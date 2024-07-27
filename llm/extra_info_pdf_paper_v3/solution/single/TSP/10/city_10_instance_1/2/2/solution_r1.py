import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
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

# Distance matrix calculation
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Minimum Spanning Tree (MST) using scipy
mst = minimum_spanning_tree(dist_matrix)

def find_odd_degree_vertices(mst):
    # Finding vertices with odd degrees in the MST
    mst = csr_matrix(mst)
    degrees = np.array(mst.sum(axis=0))[0] + np.array(mst.sum(axis=1).T)[0]
    odd_vertices = np.where(degrees % 2 == 1)[1]
    return odd_vertices

odd_vertices = find_odd_degree_vertices(mst)

# Greedy matching for odd degree vertices
def greedy_matching(odd_vertices, dist_matrix):
    matches = []
    while odd_vertices:
        i = odd_vertices.pop()
        if odd_vertices:
            distances = [(dist_matrix[i, j], j) for j in odd_vertices]
            _, closest = min(distaurants, key=lambda x: x[0])
            matches.append((i, closest))
            odd_vertices.remove(closest)
    return matches

matching = greedy_matching(list(odd_vertices), dist_matrix)

# Add edges from matching to the MST
mst_full = csr_matrix(mst)
for i, j in matching:
    mst_full[i, j] = dist_matrix[i, j]
    mst_full[j, i] = dist_matrix[j, i]

# Create an Eulerian circuit
def eulerian_circuit(mst):
    graph = csr_matrix(mst)
    n, labels = connected_components(csgraph=graph, directed=False, return_labels=True)
    tour = []
    stack = [0]
    visited = np.zeros(graph.shape[0], dtype=bool)
    while stack:
        node = stack[-1]
        neighbors = graph.indices[graph.indptr[node]:graph.indptr[node+1]]
        found = False
        for neighbor in neighbors:
            if graph[node, neighbor] != 0:
                stack.append(neighbor)
                graph[node, neighbor] = 0
                graph[neighbor, node] = 0
                found = True
                break
        if not found:
            tour.append(stack.pop())
    return tour[::-1]

tour = eulerian_circuit(mst_full)

# Convert to Hamiltonian circuit
def to_hamiltonian(tour):
    seen = set()
    path = []
    for city in tour:
        if city not in seen:
            path.append(city)
            seen.add(city)
    path.append(path[0])  # appending the starting city to end
    return path

ham_tour = to_hamiltonian(tour)

# Calculate the final cost
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

cost = tour_cost(ham_tour, dist_matrix)

# Display the tour and its cost
print(f"Tour: {ham_tour}")
print(f"Total travel cost: {cost}")