import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment

def calculate_distance(points):
    """ Calculate the Euclidean distance matrix between points """
    return squareform(pdist(points, metric='euclidean'))

def find_odd_vertex_indices(sst):
    """Find vertices of odd degree in the shortest spanning tree (SST)."""
    degree = np.sum(sst != 0, axis=1)
    odd_vertices = np.where(degree % 2 == 1)[0]
    return odd_vertices

def minimum_cost_perfect_matching(cost_matrix, odd_vertices):
    """Calculate minimum-cost perfect matching."""
    sub_matrix = cost_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(sub_matrix)
    return odd_vertices[row_ind], odd_vertices[col_ind]

def construct_eulerian_circuit(graph, start_vertex):
    """Construct an Eulerian circuit from a given Eulerian graph starting at start_vertex."""
    path = []
    stack = [start_vertex]
    while stack:
        top = stack[-1]
        # Find a non-zero edge to traverse
        neighbors = np.where(graph[top] > 0)[0]
        if neighbors.size > 0:
            next_vertex = neighbors[0]
            # Traverse the edge
            stack.append(next_vertex)
            # Remove the edge by decrementing the count
            graph[top, next_vertex] -= 1
            graph[next_vertex, top] -= 1
        else:
            path.append(stack.pop())
    return path

def solve_tsp_heuristic(cities):
    # Calculate distance matrix
    distance_matrix = calculate_distance(cities)

    # Compute shortest spanning tree (SST)
    sst = minimum_spanning_tree(distance_matrix).toarray().astype(float)
    
    # Find vertices with odd degree in the SST
    odd_vertices = find_odd_vertex_indices(sst)
    
    # Compute minimum cost perfect matching on the subgraph induced by odd degree vertices
    match1, match2 = minimum_cost_perfect_matching(distance_all, tree)
    # Add matching edges to SST
    for i, j in zip(match1, match2):
        sst[i, j] = distance_matrix[i, j]
        sst[j, i] = distance_matrix[i, j]
    
    # Construct Eulerian circuit
    eulerian_circuit = construct_eulerian_circuit(np.ceil(sst).astype(int), 0)

    # Make the tour Hamiltonian by removing repeated nodes
    visited = set()
    hamiltonian_circuit = [city for city in eulerian_circuit if not (city in visited or visited.add(city))]

    # Ensure tour starts and ends at the depot
    hamiltonian_circuit.append(hamiltonian_circuit[0])

    # Calculate total travel cost
    total_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

    return hamiltonian_circuit, total_cost

# Define city coordinates
cities = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Compute the shortest tour and its cost
tour, cost = solve_transition_point_medics(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", cost)