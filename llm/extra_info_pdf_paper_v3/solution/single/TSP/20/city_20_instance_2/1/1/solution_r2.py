import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 != 0]

def minimum_weight_perfect_matching(G, odd_deg_vertices):
    subgraph = G.subgraph(odd_deg_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight="weight")

def create_eulerian_circuit(G, start_vertex):
    return list(nx.eulerian_circuit(G, source=start_vertex))

def compute_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Create a complete graph
N = len(cities)
distance_matrix = [[0] * N for _ in range(N)]
G = nx.Graph()
for i in range(N):
    for j in range(i + 1, N):
        distance = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = distance_matrix[j][i] = distance
        G.add_edge(i, j, weight=distance)

# Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Find odd degree vertices
odd_degree_vertices = find_odd_degree_vertices(mst)

# Minimum-Cost Perfect Matching
matching = minimum_weight_perfect_matching(G, odd_degree_vertices)

# Create a multigraph by combining the MST and the matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(list(matching))

# Create the Eulerian circuit from the multigraph
eulerian_circuit = create_eulerian_circuit(multi_graph, 0)

# Convert Eulerian circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_path = []
for u, _ in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_path.append(u)

hamiltonian_path.append(0)  # returning to the starting point

# Calculate the cost of the tour
tour_cost = compute_tour_cost(hamiltonian_path, distance_matrix)

print("Tour:", hamiltonian_path)
print("Total travel cost:", tour_cost)