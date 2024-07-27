import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
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

    # Step 1: Compute Minimum Spanning Tree (MST)
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst_matrix = mst_matrix.toarray()
    mst_matrix_symmetric = mst_matrix + mst_matrix.T  # ensure symmetry

    # Step 2: Find all vertices with odd degree in the MST to form set O
    degrees = np.sum(mst_matrix_symmetric > 0, axis=1)
    odd_degree_vertices = np.where(degrees % 2 == 1)[0]

    # Step 3: Minimum weight perfect matching M in the subgraph induced by O
    # Placeholder to demonstrate, requires proper perfect matching handling
    # Step is highly complex and generally requires specialized algorithms like Blossom V
    # For simplicity here, we just create a dummy half-perfect match if odd vertices > 1
    if len(odd_degree_vertices) > 1:
        min_cost_match = [(odd_degree_vertices[i], odd_degree_vertices[i-1])
                          for i in range(1, len(odd_degree_vertices), 2)]
        for i, j in min_cost_match:
            mst_matrix_symmetric[i][j] = dist_matrix[i][j]
            mst_matrix_symmetric[j][i] = dist_matrix[j][i]

    # Step 4, 5, 6: Form Eulerian circuit from MST and matching set
    # Simplified as tour reconstruction (does not handle multiple odd nodes robustly)
    path = [0]
    visited = set()

    def visit(v):
        for i in range(num_cities):
            if mst_matrix_symmetric[v][i] > 0 and i not in visited:
                visited.add(i)
                path.append(i)
                mst_matrix_symmetric[v][i] = mst_matrix_symmetric[i][v] = 0  # remove edge
                visit(i)
                path.append(v)  # backtrack to v

    visited.add(0)
    visit(0)

    path.append(0)  # complete the tour by returning to the depot

    # Removing repeated visits to same cities (converting to Hamiltonian path)
    seen = set()
    hamiltonian_path = []
    for city in path:
        if city not in seen or city == 0:
            hamiltonian_path.append(city)
            seen.add(city)

    # Calculate total cost
    total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

    return hamiltonian_path, total_cost

# Define cities coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

tour, cost = christofides_algorithm(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")