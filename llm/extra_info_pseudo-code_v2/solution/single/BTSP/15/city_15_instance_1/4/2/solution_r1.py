import math
import networkx as nx

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initialize_cities():
    return [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]

def construct_graph(cities):
    G = nx.Graph()
    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities):
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(city1, city2))
    return G

def find_bottleneck_hamiltonian_cycle(G, start_node):
    # Using Minimum Spanning Tree (MST) for an approximation method
    mst = list(nx.minimum_spanning_edges(G, data=True))
    mst_graph = nx.Graph()
    mst_graph.add_edges_from(mst)
    mst_graph = nx.MultiGraph(mst_graph)  # Make sure it's treated as undirected
    eulerian_circuit = list(nx.eulerian_circuit(nx.eulerize(mst_graph), source=start_node))
    # Make hamiltonian by skipping visited nodes
    visited = set()
    hamiltonian_cycle = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_cycle.append(u)
        if v not in visited:
            visited.add(v)
            hamiltonian_cycle.append(v)
    hamiltonian_cycle.append(hamiltonian_cycle[0])  # to complete the cycle
    return hamiltonian_cycle

cities = initialize_cities()
graph = construct_graph(cities)
tour = find_bottleneck_hamiltonian_cycle(graph, start_node=0)

# Calculate distances on the tour
tour_distances = [graph[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1)]
total_cost = sum(tour_distances)
max_distance = max(tour_distances, default=0)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))