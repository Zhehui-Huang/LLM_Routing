import math
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Cities coordinates
coordinates = [
    (84, 67),  # Depot 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Minimum Spanning Tree (MST)
def compute_mst(graph):
    return nx.minimum_spanning_tree(graph, weight="weight")

# Minimum Weight Perfect Matching
def compute_min_weight_matching(graph, odd_vertices):
    # Subgraph for the odd degree vertices
    subgraph = graph.subgraph(odd_vertices)
    distances = distance_matrix(list(nx.get_node_attributes(subgraph, 'pos').values()), 
                                list(nx.get_item_attributes(subgraph, 'pos').values()))
    row_ind, col_ind = linear_sum_assignment(distances)
    matching = nx.Graph()
    for row, column in zip(row_ind, col_ind):
        u, v = odd_vertices[row], odd_vertices[column]
        if u != v:
            matching.add_edge(u, v, weight=distances[row][column])
    return matching

# Christofides Algorithm 
def christofides_algorithm(coordinates):
    # Step 1: Building the complete graph
    num_cities = len(coordinates)
    graph = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            graph.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

    # Step 2: Minimum Spanning Tree
    mst = compute_mst(graph)

    # Step 3: Find vertices with odd degree
    odd_degree_vertices = [v for v in mst.nodes if mst.degree[v] % 2 != 0]

    # Step 4: Minimum Weight Perfect Matching on the subgraph of odd degree vertices
    matching = compute_min_weight_matching(graph, odd_degree_vertices)

    # Step 5: Combine MST and matching
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching.edges(data=True))

    # Step 6: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Convert to Hamiltonian path, skipping visited nodes
    visited = set()
    hamiltonian_path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_path.append(u)
    hamiltonian_path.append(hamiltonian_path[0])

    # Calculating the total cost of the path
    total_cost = sum(graph[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

    return hamiltonian_path, total_cost

# Compute tour and cost using Christofides algorithm
tour, total_cost = christofides_algorithm(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)