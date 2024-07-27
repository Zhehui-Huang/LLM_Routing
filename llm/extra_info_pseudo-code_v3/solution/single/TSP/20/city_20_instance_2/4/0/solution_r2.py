import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_graph(coords):
    G = nx.Graph()
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(coords[i], coords[j]))
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def get_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subG = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True, weight='weight')

def create_multigraph(T, M):
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    return multigraph

def find_eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))

def shortest_hamiltonian_circuit(circuit, start_node):
    path = [start_node]
    visited = set([start_node])
    for u, v in circuit:
        if v not in visited:
            visited.add(v)
            path.append(v)
    path.append(start_node)  
    return path

def calculate_tour_cost(path, coords):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += euclidean_distance(coords[path[i]], coords[path[i+1]])
    return total_distance

# Coordinates of the cities including depot city 0
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

G = construct_graph(coords)
T = find_minimum_spanning_tree(G)
odd_degree_vertices = get_odd_degree_vertices(T)
M = minimum_weight_perfect_matching(G, odd_degree_vertices)
H = create_multigraph(T, M)
circuit = find_eulerian_circuit(H)
tour = shortest_hamiltonian_circuit(circuit, 0)
tour_cost = calculate_tour_cost(tour, coords)

# Displaying the results
print("Tour:", tour)
print("Total travel cost:", tour_cost)