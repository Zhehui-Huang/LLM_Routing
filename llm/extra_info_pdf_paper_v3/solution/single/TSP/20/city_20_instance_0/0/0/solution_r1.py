import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
from itertools import combinations

# Define cities along with depot city
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Calculate the Euclidean distance matrix
coords = np.array(list(cities.values()))
distance_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a minimum spanning tree (MST)
mst = minimum_spanning_tree(distance_matrix).toarray()

# Function to find odd degree vertices in the MST
def find_odd_vertices(mst):
    degree = np.sum(mst > 0, axis=0) + np.sum(mst > 0, axis=1)
    odd_vertices = np.where(degree % 2 == 1)[0]
    return odd_vertices

odd_vertices = find_odd_vertices(mst)
num_vertices = len(odd_vertices)

# Function to find the Minimum-Cost Perfect Matching among odd degree vertices
def perfect_matching(odd_ver):
    min_total_cost = np.inf
    best_matching = []
    for pairings in combinations(range(num_vertices), num_vertices // 2):
        matches = list(pairings) + list(set(range(num_vertices)) - set(pairings))
        pair_cost = sum(distance_matrix[odd_ver[matches[i]], odd_ver[matches[i+1]]] for i in range(0, num_vertices, 2))
        
        if pair_cost < min_total_cost:
            min_total_cost = pair_cost
            best_matching = matches
    return best_matching

matching = perfect_matching(odd_vertices)

# Combine MST and Perfect Matching to create an Eulerian Circuit
euler_mst = csr_matrix(mst)
for i in range(0, num_vertices, 2):
    euler_mst[odd_vertices[matching[i]], odd_vertices[matching[i+1]]] += 1
    euler_mst[odd_vertices[matching[i+1]], odd_vertices[matching[i]]] += 1

# Eulerian circuit to Hamiltonian Circuit
def eulerian_to_hamiltonian(mst):
    n, components = connected_components(mst, directed=False)
    path = []
    visited = set()

    def visit(vertex):
        path.append(vertex)
        visited.add(vertex)

        for adj in range(len(cities)):
            if mst[vertex, adj] > 0 and adj not in visited:
                mst[vertex, adj] -= 1
                mst[adj, vertex] -= 1
                visit(adj)

    visit(0)  # starting at the depot city
    path.append(0)  # end at the depot city
    return path

tour = eulerian_to_hamiltonian(euler_mst)

# Calculate the travel cost of the tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

total_cost = calculate_tour_cost(tour, distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")