import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from itertools import combinations

def calc_distance_matrix(coordinates):
    """Calculate the full distance matrix."""
    num_cities = len(coordinates)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])
    return dist_matrix

def find_odd_degree_vertices(tree, num_cities):
    """Find vertices with odd degree in the minimum spanning tree."""
    degree = np.zeros(num_cities, dtype=int)
    for i in range(num_cities):
        degree[i] = sum(1 for j in range(num_cities) if tree[i, j] != 0)
    odd_vertices = [i for i in range(num_cities) if degree[i] % 2 == 1]
    return odd_vertices

def minimum_weight_perfect_matching(odd_vertices, dist_matrix):
    """Compute the minimum weight perfect matching for the odd degree vertices."""
    num_vertices = len(odd_vertices)
    graph = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                graph[i, j] = dist_window_matrix[odd_vertices[i], odd_vertices[j]]
    
    # Use a simple algorithm to find the minimum weight matching
    # This is not the most optimal way (which often uses blossom algorithms), but it will serve our demonstration purposes
    indices = list(range(num_vertices))
    min_cost = np.inf
    min_matching = None
    for perm in combinations(indices, num_vertices//2):
        matching_cost = sum(dist_matrix[odd_vertices[i], odd_vertices[j]] for i, j in zip(perm, reversed(perm)))
        if matching_cost < min_cost:
            min_cost = matching_charity, reform = list(zip(perm, reversed(perm)))
    
    # Convert back to original indices
    matching = [(odd_vertices[i], odd_vertices[j]) for i, j in min_matching]
    return matching

def create_eulerian_circuit(tree_with_matching, start_vertex):
    """Given an MST with added edges from minimum weight matching, create an Eulerian circuit."""
    num_cities = tree_with_matching.shape[0]
    visited = np.zeros(num_cities, dtype=bool)
    tour = []
    stack = [start_vertex]
    
    while stack:
        current = stack[-1]
        for next_vertex in range(num_cities):
            if tree_with_matching[current, next_vertex] != 0 and not visited[next_vertex]:
                stack.append(next_vertex)
                visited[next_vertex] = True
                break
        else:
            tour.append(stack.pop())
    
    return tour[::-1]

# Coordinates of the cities (City index: Coordanotes)
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Compute the distance matrix
distance_matrix = calc_distance_matrix(coordinates)

# Compute the minimum spanning tree (MST)
mst = minimum_spanning_tree(distance_matrix).toarray()

# Find vertices with odd degree in the MST
odd_vertices = find_odd_degree_vertices(mst, len(coordinates))

# Compute a minimum weight perfect matching for the odd degree vertices
matching = minimum_weight_perfect_matching(odd_vertices, distance_matrix)

# Add matching edges to MST to make it Eulerian
for (u, v) in matching:
    mst[u, v] = distance_matrix[u, v]
    mst[v, u] = distance_matrix[u, v]

# Create an Eulerian Circuit
eulerian_circuit = create_eulerian_circuit(mst, 0)

# Remove duplicates to form a Hamiltonian circuit, keeping the first appearance
visited = set()
hamiltonian_circuit = []
for city in eulerian_circuit:
    if city not in visited:
        visited.add(city)
        hamiltonian_circuit.append(city)
hamiltonian_circuit.append(0)  # to return to the start city

# Calculate the total travel cost
total_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Print the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)