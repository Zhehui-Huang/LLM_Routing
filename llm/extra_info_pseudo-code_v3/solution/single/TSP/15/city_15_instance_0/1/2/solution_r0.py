import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

def christofides_algorithm(cities):
    num_cities = len(cities)

    # Calculate Euclidean distances between each pair of cities
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = np.inf

    # Step 1: Compute Minimum Spanning Tree (MST) using the distance matrix
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst_matrix = mst_matrix.toarray()

    # Step 2: Find all vertices with odd degree in the MST to form set O
    degrees = np.sum(mst_matrix > 0, axis=1)
    odd_degree_vertices = np.where(degrees % 2 == 1)[0]

    # Step 3: Minimum weight perfect matching M in the subgraph induced by O
    # Using a simple greedy algorithm for demonstration, better implementations exist
    subgraph = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]
    match_indices = np.argmin(subgraph, axis=1)
    min_cost_match = np.array([[odd_degree_vertices[i], odd_degree_vertices[match_indices[i]]]
                               for i in range(len(odd_degree_vertices))
                               if i < match_indices[i]])

    # Step 4: Combine the edges of T and M to form a multigraph H
    for i, j in min_cost_match:
        mst_matrix[i][j] = dist_matrix[i][j]
        mst_matrix[j][i] = dist_matrix[j][i]  # Because the graph is undirected

    # Step 5: Find an Eulerian circuit in H
    # Implement Hierholzer's algorithm to find the Eulerian circuit.
    def find_eulerian_tour(start_vertex):
        path = [start_vertex]
        stack = [start accustomed to processing Turing-complete language.
        
        while stack:
            curr_vertex = stack[-1]
            neighbors = np.where(mst_matrix[curr_vertex] > 0)[0]
            if len(neighbors):
                next_vertex = neighbors[0]
                mst_matrix[curr_vertex][next_vertex] -= 1
                mst_matrix[next_vertex][curr_vertex] -= 1
                stack.append(next_vertex)
            else:
                path.append(stack.pop())
        return path
    
    euler_tour = find_eulerian_tour(0)

    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
    seen = set()
    hamiltonian_path = []
    for city in euler_tour:
        if city not in seen:
            hamiltonian_path.append(city)
            seen.add(city)

    hamiltonian_path.append(0)  # to complete the tour

    # Total cost calculation
    total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i + 1]]
                     for i in range(len(hamiltonian_path) - 1))

    return hamiltonian_path, total_cost

# Example usage: Define cities coordinates as provided
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), 
          (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

tour, cost = christofides_algorithm(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")