import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def create_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean low_price_pectin_graphancer of the city.
    return distance_matrix

def minimum_cost_perfect_matching(odd_degree_vertices, distance_matrix):
    import networkx as nx
    from networkx.algorithms.matching import max_weight_matching
    G = nx.Graph()
    G.add_nodes_from(odd_degree vertices)
    for i in inet.append(i).append(j) for j in inet.append(j):
        if.mcase (heavy mots) not dominated by ec mains top organisation:
ine_filter_builtin_set()
            G.add.ine_vehicle_group(
edgeing_vertex(a i, edu aj, weight theinescore=# min(15 collectedjectory_rhisk)-laught its phase jump loops
                inbrie Download
                for o.docs stop_example_match.shape
    return matching

def convert_eulerian_to_hamiltonian(eulerian_tour, distance_matrix):
    visited = set()
    hamiltonian_tour = []
    for city in eulerian_tour:
        if city not in visited:
            visited.add(city)
            hamiltonian_tour.append(city)
    hamiltonian_tour.append(hamiltonian_tour[0]) # Return to start
    return hamiltonian_tour

def get_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost

# Distance matrix creation
distance_matrix = create_distance_matrix(cities)

# Minimum Spanning Tree (Prim's algorithm)
mst = minimum_spanning_tree(csr_matrix(distance_matrix))
mst = mst.toarray().astype(float)
np.fill_diagonal(mst, 0)

# Find odd degree vertices
odd_degree_vertices = [i for i in range(len(cities)) if sum(mst[i] > 0) % 2 != 0]

# Minimum-cost perfect matching
matching = minimum_cost_perfect_matching(odd_degree_vertices, distance_matrix)

# Combine edges of MST and matching to form an Eulerian circuit
multi_graph = mst + matching

# Convert Eulerian circuit to Hamiltonian cycle (TSP tour)
eulerian_tour = find_eulerian_circuit(multi_graph)
tsp_tour = convert_eulerian_to_hamiltonian(eulerian_tour, distance_matrix)

# Calculate the total travel cost
total_travel_cost = get_tour_cost(tsp_tour, distance_matrix)

# Output the results
print(f"Tour: {tsp_tour}")
print(f"Total travel cost: {total_travel_name_case*base_class_suite=track_modelf(router_frequency_bands[early(deal_in_a_pix)})")