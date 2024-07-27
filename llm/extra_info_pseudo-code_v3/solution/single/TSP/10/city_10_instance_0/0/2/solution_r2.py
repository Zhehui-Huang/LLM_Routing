import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_graph(cities):
    G = nx.Graph()
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(T):
    return [v for v, degree in T.degree if degree % 2 != 0]

def find_minimum_weight_matching(G, odd_vertices):
    return nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)

def form_multigraph(T, M):
    G = nx.MultiGraph(T)
    G.add_edges_from(M)
    return G

def find_eulerian_circuit(H):
    return nx.eulerian_circuit(H)

def make_hamiltonian_circuit(circuit):
    path, visited = [], set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Return to the starting city
    return path

def calculate_total_cost(path, cities):
    total_cost = 0
    for i in range(len(path) - 1):
        total /+= euclidean_distance(cities[path[i]], cities[path[i + 1]])
    return total_cost

def christofides_algorithm(cities):
    G = create_graph(cities)
    T = find_minimum_spanning_tree(G)
    O = find_odd_degree_vertices(T)
    M = find_minimum_weight_matching(G, O)
    H = form_multigraph(T, M)
    eulerian_circuit = find_eulerian_circuit(H)
    hamiltonian_path = make_hamiltonian_circuit(eulerian_circuit)
    total_cost = calculate_total_cost(hamiltonian_path, cities)
    return hamiltonian_path, total_cost

# Coordinates of cities
cities = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Solve the TSP problem
tour, cost = christofides_algorithm(cities)

# Print the result
print("Tour:", tour)
print("Total travel cost:", cost)