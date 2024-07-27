import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                distances[(i, j)] = dist
    return distances

cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def create_graph(cities, distances):
    G = nx.Graph()
    for i, j in distances:
        G.add_edge(i, j, weight=distances[(i, j)])
    return G

def find_tour(cities):
    distances = calculate_distances(cities)
    G = create_graph(cities, distances)
    
    # Find MST
    mst = nx.minimum_spanning_tree(G)
    
    # Find odd degree vertices
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
    
    # Create subgraph for perfect matching
    subgraph = nx.Graph()
    subgraph.add_nodes_from(odd_degree_nodes)
    for i in odd_degree_nodes:
        for j in odd_degree_nodes:
            if i != j:
                subgraph.add_edge(i, j, weight=distances[(i, j)])
    
    # Find minimum weight matching to create an Eulerian circuit
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Add matching edges to MST
    mst.add_edges_from(matching)
    
    # Create Eulerian circuit
    eulerian_tour = list(nx.eulerian_circuit(mst, source=0))
    
    # Remove repeated nodes to form a Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = []
    for x, y in eulerian_tour:
        if x not in visited:
            visited.add(x)
            hamiltonian_circuit.append(x)
    hamiltonian_circuit.append(0)  # complete the tour by coming back to the start
    
    # Calculate tour distance
    total_distance = sum(distances[(hamiltonian_circuit[i], hamiltonian_circuit[i+1])] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_distance

# Get the tour and travel cost
tour, total_travel_cost = find_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)