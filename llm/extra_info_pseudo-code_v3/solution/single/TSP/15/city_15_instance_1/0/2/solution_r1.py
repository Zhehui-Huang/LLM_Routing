import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.optimize import linear_sum_assignment
from collections import defaultdict, deque

# Helper functions
def compute_mst(cost_matrix):
    tree = minimum_spanning_tree(cost_matrix)
    return tree.toarray().astype(float)

def find_odd_degree_vertices(mst):
    return [i for i in range(len(mst)) if sum((mst[i, :] > 0) + (mst[:, i] > 0)) % 2 != 0]

def perfect_matching(subgraph, odd_vertices):
    num_vertices = len(odd_vertices)
    optimal_match_cost = np.full((num_vertices, num_vertices), np.inf)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            optimal_match_cost[i, j] = subgraph[odd_vertices[i], odd_vertices[j]]
            optimal_match_cost[j, i] = subgraph[odd_vertices[i], odd_vertices[j]]
    row_ind, col_ind = linear_sum_assignment(optimal_match_cost)
    matches = [(odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]) for i in range(num_vertices) if row_ind[i] < col_ind[i]]
    return matches

def create_multigraph(mst, perfect_matches):
    multigraph = np.copy(mst)
    for i, j in perfect_matches:
        multigraph[i][j] += 1
        multigraph[j][i] += 1
    return multigraph

def find_eulerian_circuit(adj_matrix):
    num_vertices = len(adj_matrix)
    graph = defaultdict(list)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[i][j] > 0:
                graph[i].append(j)
    
    # Find Eulerian circuit using Hierholzer’s Algorithm
    current_vertex = 0  # Starting from depot
    circuit = []
    path = [0]
    while path:
        if graph[current_vertex]:
            next_vertex = graph[current_vertex].pop()
            path.append(next_vertex)
            current_vertex = next_vertex
        else:
            circuit.append(current_vertex)
            current_vertex = path.pop()
    return circuit[::-1]

def convert_to_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    hamiltonian_circuit = []
    for vertex in eulerian_circuit:
        if vertex not in visited:
            hamiltonian_circuit.append(vertex)
            visited.add(vertex)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # To return to the start point
    return hamiltonian_circuit

coordinates = np.array([
    [29, 51], [49, 20], [79, 69], [17, 20], [18, 61],
    [40, 57], [57, 30], [36, 12], [93, 43], [17, 36],
    [4, 60], [78, 82], [83, 96], [60, 50], [98, 1]
])

dist_matrix = distance_matrix(coordinates, coordinates)
mst = compute_mst(dist_matrix)
odd_vertices = find_odd_degree_vertices(mst)
perfect_matches = perfect_matching(dist_matrix, odd_vertices)
multigraph = create_multigraph(mst, perfect_matches)
eulerian_circuit = find_eulerian_circuit(multigraph)
hamiltonian_circuit = convert_to_hamiltonian_circuit(eulerian_circuit)

# Calculate tour cost
tour_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", tour_cost)