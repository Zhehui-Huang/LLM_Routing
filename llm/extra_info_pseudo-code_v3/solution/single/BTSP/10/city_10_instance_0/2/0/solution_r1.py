import math
import itertools
import networkx as nx

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_graph_with_threshold(threshold, edges):
    g = nx.Graph()
    g.add_nodes_from(range(len(positions)))
    for (i, j, d) in edges:
        if d <= threshold:
            g.add_edge(i, j)
    return g

def heuristic_hamiltonian_path_check(graph):
    if nx.is_connected(graph):
        try:
            path = nx.approximation.traveling_salesman_problem(graph, cycle=False)
            if len(path) == len(positions):
                return path
        except nx.NetworkXError:
            pass
    return None

# Node positions
positions = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), 
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Building the complete graph with distances
edges = []
for i, j in itertools.combinations(range(len(positions)), 2):
    dist = calculate_distance(positions[i], positions[j])
    edges.append((i, j, dist))
    edges.append((j, i, dist))
edges = sorted(edges, key=lambda x: x[2])

# Get thresholds from edge weights
thresholds = sorted(set(edge[2] for edge in edges))

# Seek for the lightest maximal weight that allows a Hamiltonian path
for threshold in thresholds:
    graph = create_graph_with_threshold(threshold, edges)
    hamiltonian_path = heuristic_hamiltonian_path_check(graph)
    if hamiltonian_path:
        # Ensure it starts and ends at the depot (0)
        if hamiltonian_path[0] != 0:
            hamiltonian_path = list(reversed(hamiltonian_path))
        if hamiltonian_path[-1] != 0:
            hamiltonian_path.append(0)
        max_edge_weight = max(calculate_distance(positions[hamiltonian_path[i]], positions[hamiltonian_path[i+1]]) for i in range(len(hamiltonian_path) - 1))
        total_distance = sum(calculate_distance(positions[hamiltonian_path[i]], positions[hamiltonian_path[i+1]]) for i in range(len(hamiltonian_path) - 1))
        print(f"Tour: {hamiltonian_path}")
        print(f"Total travel cost: {total_distance:.2f}")
        print(f"Maximum distance between consecutive cities: {max_edge_weight:.2f}")
        break
else:
    print("No Hamiltonian path found")