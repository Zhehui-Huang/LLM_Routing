import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.optimize import linear_sum_assignment

def solve_tsp(coordinates):
    # Calculate the Euclidean distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)

    # Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(dist_matrix)
    mst = mst.toarray()
    mst[mst == 0] = np.inf

    # Find vertices with odd degree
    odd_degree = (mst != np.inf).sum(axis=0) % 2 == 1
    odd_vertices = np.where(odd_degree)[0]

    if len(odd_vertices) > 1:  # Check necessary for MCPM
        subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
        row_ind, col_ind = linear_sum_assignment(subgraph)
        mst = mst + dist_matrix  # revert infinities in MST to original distances

        # Adding minimum-cost perfect matching edges to the MST 
        for i, j in zip(row_ind, col_ind):
            u, v = odd_vertices[i], odd_vertices[j]
            mst[u][v] = dist_matrix[u][v]
            mst[v][u] = dist_matrix[v][u]

    # Finding an Eulerian circuit made simple
    visited = np.zeros(len(coordinates), dtype=bool)
    circuit = []
    stack = [0]  # start from depot

    while stack:
        u = stack[-1]
        all_adjacent = np.where(mst[u] < np.inf)[0]  # all connected cities from u
        neighbors = [v for v in all_adjacent if mst[u][v] < np.inf]
        
        if not neighbors:
            circuit.append(stack.pop())
        else:
            stack.append(neighbors[0])
            mst[u][neighbors[0]] = np.inf  # remove this edge
            mst[neighbors[0]][u] = np.inf  # bidirectional

    # Ensure the circuit forms a tour starting and ending at depot
    if circuit[0] != 0 or circuit[-1] != 0:
        circuit.append(0)

    # Calculate the total cost of the circuit/tour
    total_cost = sum(dist_matrix[circuit[i], circuit[i + 1]] for i in range(len(circuit) - 1))

    return circuit, total_cost

# Given coordinates for the problem
cities_coordinates = np.array([
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
])

tour, total_cost = solve_tsp(cities_coordinates)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)