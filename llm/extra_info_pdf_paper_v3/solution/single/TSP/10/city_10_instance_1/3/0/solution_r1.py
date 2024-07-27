import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def christofides_tour(coordinates):
    num_cities = len(coordinates)
    
    # Step 1: Calculate distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Step 2: Minimum Spanning Tree (MST)
    mst_matrix = minimum_spanning_tree(dist_matrix).toarray()
    mst_matrix = mst_matrix + mst_matrix.T  # Make it symmetric to include all edges of MST
    
    # Step 3: Find odd degree vertices
    odd_vertices = [i for i in range(num_cities) if np.sum(mst_matrix[i] != 0) % 2 != 0]
    
    # Step 4: Minimum Cost Perfect Matching (MCPM) on odd degree vertices
    subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(subgraph)
    
    # Adding MCPM edges to the MST
    for i, j in zip(row_ind, col_ind):
        mst_matrix[odd_vertices[i], odd_vertices[j]] = dist_matrix[odd_vertices[i], odd_vertices[j]]
        mst_matrix[odd_vertices[j], odd_vertices[i]] = dist_matrix[odd_vertices[j], odd_vertices[i]]
    
    # Step 5: Convert the graph to an Eulerian tour
    eulerian_tour = []
    visited = []
    stack = [0]

    while stack:
        u = stack[-1]
        unvisited_neighbors = [v for v in range(num_cities) if mst_matrix[u, v] != 0 and v not in visited]
        if unvisited_neighbors:
            stack.append(unvisited_neighbors[0])
            visited.append(unvisited_neighbors[0])
        else:
            eulerian_tour.append(stack.pop())  # Complete the circuit back at the depot
    
    # Step 6: Make the Eulerian tour Hamiltonian and calculate total cost
    hamiltonian_tour = []
    visited = np.zeros(num_cities, dtype=bool)
    total_cost = 0
    current_city = eulerian_tour[0]

    for city in eulerian_tour:
        if not visited[city]:
            hamiltonian_tour.append(city)
            total_cost += dist_matrix[current_city, city]
            visited[city] = True
            current_city = city

    # Returning to the start point
    hamiltonian_tour.append(0)
    total_cost += dist_matrix[hamiltonian_tour[-2], 0]

    return hamiltonian_tour, total_cost

# Fixed coordinates
coordinates = np.array([(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91),
                        (70, 14), (97, 44), (17, 69), (95, 89)])

tour, cost = christofides_tour(coordinates)

# Output the results in the specified format
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")