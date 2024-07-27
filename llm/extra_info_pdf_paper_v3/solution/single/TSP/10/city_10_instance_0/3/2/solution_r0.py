import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment

def calculate_distance(points):
    """ Calculate the Euclidean distance matrix between points """
    return squareform(pdist(points, metric='euclidean'))

def find_odd_vertex_indices(sst):
    """ Find vertices of odd degree in the shortest spanning tree (SST) """
    odd_vertices = np.where(np.sum(np.array(sst) != 0, axis=1) % 2 == 1)[0]
    return odd_vertices

def minimum_cost_perfect_matching(cost_matrix, odd_vertices):
    """ Calculate minimum-cost perfect matching """
    sub_matrix = cost_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(sub_matrix)
    return odd_vertices[row_ind], odd_vertices[col_ind]

def construct_eulerian_circuit(graph, start_vertex):
    """ Convert Eulerian tour to Hamiltonian circuit using shortcutting """
    n_vertices = len(graph)
    visited = np.zeros(n_vertices, dtype=bool)
    path = []
    stack = [start_vertex]
    
    while stack:
        u = stack[-1]
        next_vertices = [v for v in range(n_vertices) if graph[u, v] > 0]
        
        if not next_vertices:
            if len(path) == 0 or u != path[-1]:
                path.append(u)
            stack.pop()
        else:
            v = next_vertices[0]
            graph[u, v] -= 1
            graph[v, u] -= 1
            stack.append(v)

    return path

def solve_tsp_heuristic(cities):
    # Calculate distance matrix
    distance_matrix = calculate_to_distance(cities)

    # Compute shortest spanning tree (SST)
    mst = minimum_spanning_tree(distance_matrix).toarray().astype(float)
    
    # Find the vertices with odd degree
    odd_vertices = find_odd_vertex_indices(mst)
    
    # Compute minimum cost perfect matching on the subgraph induced by odd degree vertices
    matches1, matches2 = minimum_cost_perfect_matching(distance_matrix, odd_vertices)
    for i, j in zip(matches1, matches2):
        mst[i, j] = distance_matrix[i, j]
        mst[j, i] = distance_matrix[i, j]
    
    # Construct Eulerian circuit and convert it to Hamiltonian path (shortcutting)
    eulerian_circuit = construct_eulerian_circuit(np.ceil(mst).astype(int), 0)
    hamiltonian_circuit = list(dict.fromkeys(eulerian_circuit)) # Remove repeated vertices but keep order
    
    # Return to starting point to complete the circuit
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    
    # Calculate total travel cost
    total_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

    return hamiltonian_circuit, total_cost

# Cities coordinates
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

# Find the shortest tour and total cost
tour, total_cost = solve_tsp_heuristic(cities)

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")