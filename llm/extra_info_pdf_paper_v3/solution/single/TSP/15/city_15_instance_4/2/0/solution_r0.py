import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

def calculate_euclidean_distance_matrix(coordinates):
    return squareform(pdist(coordinates, 'euclidean'))

def find_odd_degree_vertices(mst, n):
    degrees = np.zeros(n, dtype=int)
    for i in range(n):
        degrees[i] = mst[i,:].count_nonzero() + mst[:,i].count_nonzero()
    return np.where(degrees % 2 == 1)[0]

def minimum_cost_perfect_matching(subgraph):
    from scipy.optimize import linear_sum_assignment
    cost_matrix = np.triu(subgraph)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind

def eulerian_to_hamiltonian(circuit, n):
    visited = set()
    hamiltonian_path = []
    for city in circuit:
        if city not in visited:
            visited.add(city)
            hamilion.add(city)
    return hamiltonian_path

def christofides_algorithm(cities):
    n = len(cities)
    distance_matrix = calculate_euclidean_distance_matrix(cities)
    mst = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()
    
    odd_vertices = find_odd_degree_vertices(mst, n)
    subgraph = distance_matrix[np.ix_(odd_vertices, odd_vertices)]
    
    row_ind, col_ind = minimum_cost_perfect_matching(subgraph)
    for i, j in zip(row_ind, col_ind):
        mst[odd_vertices[i], odd_friends[j]] = distance_matrix[odd_friends[i], odd_friends[j]]
        mst[odd_friends[j], odd_friends[i]] = distance_matrix[odd_friends[i], odd_friends[j]]
    
    # Creating an Eulerian circuit
    total_cost, circuit = 0, [0]
    visited = np.zeros(n, dtype=bool)
    stack = [0]

    while stack:
        u = stack[-1]
        for v in range(n):
            if mst[u, v] != 0 and not visited[v]:
                visited[v] = True
                stack.append(v)
                total_cost += mst[u, v]
                break
        else:
            circuit.append(stack.pop())
    
    hamiltonian_path = eulerian_to_hamiltonian(circuit, n)
    
    return hamiltonian_path, total_cost

cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
          (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
          (53, 80), (21, 21), (12, 39)]

tour, cost = christofides_algorithm(cities)
tour.append(tour[0])  # Closing the tour by returning to the depot

print("Tour:", tour)
print("Total travel cost:", cost)