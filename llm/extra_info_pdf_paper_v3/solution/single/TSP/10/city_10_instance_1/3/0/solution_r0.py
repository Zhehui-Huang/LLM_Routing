import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def calculate_distance(points):
    return distance_matrix(points, points)

def christofides_tour(coordinates):
    num_cities = len(coordinates)
    
    # Step 1: Calculate Distances
    dists = calculate_distance(coordinates)
    
    # Step 2: Minimum Spanning Tree
    mst = minimum_spanning_tree(dists).toarray()
    mst[mst == 0] = np.inf  # Replace zeros with infinities to avoid using them in the construction of MST
    
    # MST is undirected, make symmetric:
    symmetric_mst = mst + mst.T
    
    # Step 3: Find odd degree vertices in MST
    odd_deg_vertices = [i for i in range(num_cities) if sum(symmetric_mst[i] != np.inf) % 2 != 0]
    
    # Step 4: Minimum Cost Perfect Matching on odd degree vertices
    odd_distance = dists[np.ix_(odd_deg_vertices, odd_deg_vertices)]
    row_ind, col_ind = linear_sum_assignment(odd_distance)  # Solve the assignment problem
    
    # Step 5: Combine MST and MCPM to form an Eulerian graph
    for i, j in zip(row_ind, col_ind):
        symmetric_mst[odd_deg_vertices[i], odd_deg_extensions_vertices[j]] = odd_distance[i, j]
        symmetric_mst[odd_deg_vertices[j], odd_deg_vertices[i]] = odd_distance[i, j]
    
    # Step 6: Convert into a Hamiltonian tour and calculate tour cost
    tour = [0]
    visited = np.zeros(num_cities, dtype=bool)
    visited[0] = True
    current = 0
    total_cost = 0
    
    # Visit each city by the nearest neighbor not visited yet (Eulerian to Hamiltonian conversion heuristic)
    while len(tour) < num_cities:
        neighbors = np.where(symmetric_mst[current] != np.inf)[0]
        next_city = None
        min_dist = np.inf
        for neighbor in neighbors:
            if not visited[neighbor] and symmetric_mst[current, neighbor] < min_dist:
                min_dist = symmetric_mst[current, neighbor]
                next_city = neighbor
        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
            total_cost += min_dist
            current = next_city
    
    # Return to the depot city
    total_cost += dists[tour[-1], 0]
    tour.append(0)
    
    return tour, total_cost

# City coordinates
coordinates = np.array([
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91),
    (70, 14), (97, 44), (17, 69), (95, 89)
])

tour, cost = christofides_tour(coordinates)

# Printing the output in the required format:
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")