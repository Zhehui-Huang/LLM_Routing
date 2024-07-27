import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

def calculate_euclidean_distance(coordinates):
    """ Calculate the Euclidean distance matrix between each pair of points. """
    return distance_matrix(coordinates, coordinates)

def find_mst(distances):
    """ Find a minimum spanning tree using the distances. Return in adjacency matrix form. """
    mst = minimum_spanning_tree(distances)
    return mst.toarray()  # make it a matrix for easier traversal

def euler_tour_from_mst(mst, start=0):
    """ Performs a DFS on the MST to construct an Eulerian tour. """
    _, preorder = depth_first_order(mst, i_start=start, directed=False)
    return preorder

def form_hamiltonian_circuit(euler_tour, start=0):
    """ Converts an Eulerian tour to a Hamiltonian circuit by visiting each node only once. """
    visited = set()
    tour = []
    for node in euler_tour:
        if node not in visited:
            visited.add(node)
            tour.append(node)
    tour.append(start)  # return to start
    return tour

def calculate_tour_cost(tour, dist_matrix):
    """ Calculate the total cost of a tour based on a distance matrix. """
    total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Given city coordinates
coordinates = np.array([
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 71), (6, 76)
])

# Calculate distance matrix for all cities
dist_matrix = calculate_euclidean_distance(coordinates)

# Find and process an MST
mst = find_mst(dist_matrix)

# Generate an Eulerian tour from the MST
euler_tour = euler_tour_from_mst(mst, start=0)

# Convert Eulerian tour to a Hamiltonian circuit (no repeated visits)
hamiltonian_tour = form_hamiltonian_circuit(euler_tour, start=0)

# Calculate the cost of the Hamiltonian circuit
tour_cost = calculate_tour_cost(hamiltonian_tour, dist_matrix)

# Output the results
print("Tour:", hamiltonian_tour)
print("Total travel cost:", tour_cost)