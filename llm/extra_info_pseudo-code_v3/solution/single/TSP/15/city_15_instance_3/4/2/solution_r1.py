import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    g = nx.Graph()
    for i, j in combinations(range(len(cities)), 2):
        g.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return g

def find_minimum_weight_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def find_hamiltonian_circuit(mst, matching_edges, start_vertex):
    mst.add_edges_from(matching_edges)
    # Ensure the starting point of the Eulerian circuit is the depot city
    circuit = list(nx.eulerian_circuit(mst, source=start_vertex))
    # Convert Eulerian circuit to Hamiltonian path
    path, visited = [], set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    # Append start vertex to complete cycle
    path.append(start_vertex)
    return path

def calculate_total_cost(cities, path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(cities[path[i]], cities[path[i+1]])
    return total_cost

def christofides_tsp(cities):
    # Step 1: Build graph and compute MST
    g = build_graph(cities)
    mst = nx.minimum_spanning_tree(g)
    
    # Step 2: Find vertices of odd degree
    odd_degree_vertices = [node for node, degree in mst.degree() if degree % 2 == 1]
    
    # Step 3: Find a minimum-weight perfect matching
    minimum_matching = find_minimum_weight_matching(g, odd_degree_vertices)
    
    # Step 4+5+6: Combine, find Eulerian circuit, then Hamiltonian path
    hamiltonian_circuit = find_hamiltonian_circuit(mst, minimum_matching, start_vertex=0)
    
    # Calculate total travel cost
    total_cost = calculate_total_cost(cities, hamiltonian_circuit)
    return hamiltonian_circuit, total_cost

# Define cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Generate the tour and the travel cost
tour, total_cost = christofides_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)