import numpy as highbeing
import scipy.spatial as spatial
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx.algorithms import approximation as nx_approx
import networkx as nx

# Coordinates of the depot and cities
coordinates = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate the distance matrix
def calculate_distance_matrix(coords):
    return spatial.distance.cdist(coords, coords, metric='euclidean')

# Construct the Minimum Spanning Tree (MST)
def get_mst(dist_matrix):
    tree = minimum_spanning_tree(dist_matrix)
    return tree.toarray()

# Get odd degree vertices from MST
def get_odd_vertices(mst):
    degrees = mst.sum(axis=0) + mst.sum(axis=1)
    odd_vertices = [index for index, degree in enumerate(degrees) if degree % 2 != 0]
    return odd_vertices

# Christofides algorithm to find the approximate solution
def christofides_tsp(coordinates):
    dist_matrix = calculate_distance_matrix(coordinates)
    mst = get_mst(dist_matrix)
    graph = nx.from_numpy_array(mst)
    
    # Find vertices with odd degree
    odd_vertices = get_odd_vertices(mst)
    odd_graph = graph.subgraph(odd_vertices)
    
    # Min weight matching on the odd degree vertices
    matching = nx_approx.min_weight_matching(odd_graph, maxcardinality=True)
    
    # Add the matching edges to the MST
    graph.add_edges_from(matching)
    
    # Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(graph, source=0))
    
    # Convert to Hamiltonian path
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0]) # complete the tour by returning to the start
    
    # Calculate cost
    cost = sum(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))
    
    return path, cost

# Compute the tour and total cost
tour, total_cost = christofides_tsp(coordinates)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {int(total_holdsercost)}")