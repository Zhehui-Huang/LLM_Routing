import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def find_eulerian_tour(edges, n, start_node):
    neighbors = {i: [] for i in range(n)}
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    tour = []
    stack = [start_node]
    current_node = start_node
    
    while stack:
        if neighbors[current_node]:
            stack.append(current_node)
            next_node = neighbors[current_node].pop()
            neighbors[next_node].remove(current_node)
            current_node = next_node
        else:
            tour.append(current_node)
            current_node = stack.pop()
    
    return tour[::-1]

def minimum_cost_perfect_matching(odd_degree_nodes, distance_matrix):
    num_nodes = len(odd_degree_nodes)
    cost_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(num_nodes):
            cost_matrix[i, j] = distance_matrix[odd_degree_nodes[i], odd_degree_nodes[j]]
    
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return [(odd_degree_nodes[row_ind[i]], odd_degree_nodes[col_ind[i]]) for i in range(num_nodes//2)]

def christofides_algorithm(coords):
    cities_count = len(coords)
    dist_matrix = squareform(pdist(coords, metric='euclidean'))
    
    # Constructing a shortest spanning tree (SST)
    mst = minimum_spanning_tree(dist_matrix).toarray()
    mst += mst.T  # Since it's undirected
    
    # Finding odd degree vertices in the MST
    degree = np.sum(mst > 0, axis=0)
    odd_degree_nodes = np.where(degree % 2 != 0)[0]
    
    # Performing minimum-cost perfect matching
    matching = minimum_cost_perfect_matching(odd_degree_nodes, dist_matrix)
    
    # Combine the edges of MST and perfect matching to form an Eulerian circuit
    edge_list = np.vstack(np.where(mst > 0)).T
    multigraph_edges = list(map(tuple, edge_list)) + matching
    
    # Find an Eulerian circuit
    euler_tour = find_eulerian_tour(multigraph_edges, cities_count, start_node=0)
    
    # Convert Eulerian circuit to Hamiltonian path by skipping visited nodes (shortcutting)
    visited = set()
    hamiltonian_cycle = []
    for node in euler_tour:
        if node not in visited or node == 0:  # allow to return to the start node
            hamiltonian_cycle.append(node)
            visited.add(node)
    
    # Calculate the travel cost of the tour
    total_cost = sum(dist_matrix[hamiltonian_cycle[i], hamiltonian_cycle[i + 1]] for i in range(len(hamiltonian_cycle) - 1))
    
    return hamiltonian_cycle, total_cost

# Define coordinates of each city including the depot city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

# Run the Christofides algorithm to find a short path
tour, total_cost = christofides_algorithm(coordinates)

# Output in the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)