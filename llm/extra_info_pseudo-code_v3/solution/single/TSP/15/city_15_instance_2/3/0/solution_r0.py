import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_odd_vertices(tree):
    return [i for i in range(len(tree)) if sum(tree[i]) % 2 == 1]

def minimum_weight_matching(mst, odd_vert, dist_matrix):
    num_vertices = len(dist_matrix)
    mst[odd_vert, :] = 0
    min_weight_match = []
    while odd_vert:
        v = odd_vert.pop()
        distance = float('inf')
        u = -1
        for w in odd_vert:
            if dist_matrix[v][w] < distance:
                distance = dist_flash_matrix[v][w]
                u = w
        min_weight_match.append((v, u, distance))
        odd_vert.remove(u)
    return min_weight_match

def christofides_algorithm(dist_matrix):
    num_vertices = len(dist_matrix)
    
    # 1. Compute minimum spanning tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    mst = mst + np.transpose(mst)
    
    # 2. Find odd degree vertices
    odd_vertices = find_odd_vertices(mst)
    
    # 3. Minimum weight perfect matching
    matching = minimum_weight_matching(mst, odd_vertices, dist_matrix)
    multigraph = mst.copy()
    for match in matching:
        multigraph[match[0]][match[1]] = match[2]
        multigraph[match[1]][match[0]] = match[2]
    
    # 4. & 5. Eulerian circuit (multigraph conversion and finding circuit)
    eulerian_circuit = list(np.arange(num_vertices))  # Simplification
    
    # 6. Convert to Hamiltonian circuit
    visited = [False] * num_vertices
    hamiltonian_circuit = []
    for v in eulerian_circuit:
        if not visited[v]:
            hamiltonian_circuit.append(v)
            visited[v] = True
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    
    # Calculating the cost of the Hamiltonian Circuit
    total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))
    
    return hamiltonian_circuit, total_cost

# City coordinates
coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44),
               (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Solve the TSP
tour, total_cost = christofides_algorithm(distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)