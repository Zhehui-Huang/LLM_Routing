import math
import networkx as nx
from heapq import heappush, heappop
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def minimum_spanning_tree(points):
    # Number of points
    n = len(points)
    # Complete graph: (weight, node1, node2)
    edges = [(euclidean_distance(points[i], points[j]), i, j)
             for i in range(n) for j in range(i + 1, n)]
    # Create a graph
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    for weight, u, v in edges:
        graph.add_edge(u, v, weight=weight)
    # Calculate MST
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    return mst

def odd_degree_vertices(mst):
    return [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

def perfect_matching(mst, graph, odd_vertices):
    # Subgraph of all odd degree vertices in the MST
    odd_graph = graph.subgraph(odd_vertices)
    # Weighted matching in the subgraph of odd vertices
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    return matching

def find_eulerian_circuit(multi_graph, start_vertex):
    return list(nx.eulerian_circuit(multi_graph, source=start_vertex))

def make_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    cost = 0
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Closing the circuit back to the start
    return path

def calculate_total_cost(path, graph):
    total_cost = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    return total_cost

def christofides_algorithm(coordinates):
    # Step 1: Create the complete graph
    graph = nx.complete_graph(len(coordinates))
    for u in graph.nodes():
        graph.nodes[u]['pos'] = coordinates[u]
    for u, v in graph.edges():
        graph.edges[u, v]['weight'] = euclidean_distance(coordinates[u], coordinates[v])

    # Step 2: Compute a minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Step 3: Find odd degree vertices in the MST
    odd_vertices = odd_degree_vertices(mst)

    # Step 4: Find minimum-weight perfect matching
    matching = perfect_matching(mst, graph, odd_vertices)

    # Step 5: Create a multigraph by combining MST and matching
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    
    # Step 6: Find an Eulerian circuit
    start_vertex = 0
    eulerian_circuit = find_eulerian_circuit(multi_graph, start_vertex)

    # Step 7: Make a Hamiltonian circuit from Eulerian circuit
    hamiltonian_circuit = make_hamiltonian_circuit(eulerian_circuit)

    # Step 8: Calculate the total travel cost
    total_cost = calculate_total_cost(hamiltonian_circuit, graph)

    return hamiltonian_circuit, total_cost

# Coordinate definition
coordinates = [
    (84, 67),  # Depot city 0
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

# Execution of Christofides' algorithm
tour, cost = christofides_algorithm(coordinates)

print("Tour:", tour)
print("Total travel cost:", cost)