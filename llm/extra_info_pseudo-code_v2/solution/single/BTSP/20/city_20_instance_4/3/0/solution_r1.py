import numpy as np
import networkx as nx

# Cities coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a weighted graph
def create_graph(coords):
    n = len(coords)
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coords[i], coords[j])
            G.add_edge(i, j, weight=dist)
    return G

# Find a Hamiltonian cycle that minimizes the maximum edge weight in the cycle
def find_approx_min_bottleneck_hamiltonian_cycle(G, start_node):
    # Minimum spanning tree using Kruskal's algorithm
    mst = list(nx.minimum_spanning_edges(G, data=True))
    mst_graph = nx.Graph()
    mst_graph.add_edges_from(mst)

    # Double tree algorithm: create a Eulerian circuit and then make it Hamiltonian
    eulerian_circuit = list(nx.eulerian_circuit(nx.eulerize(mst_graph), source=start_node))
    visited = set()
    cycle = []
    max_weight = 0

    for u, v in eulerian_circuit:
        if v not in visited:
            cycle.append(v)
            visited.add(v)
            weight = G[u][v]['weight']
            if weight > max_weight:
                max_weight = weight

    cycle.append(start_node)  # return to the start node

    return cycle, max_weight

# Create graph from city coordinates
G = create_graph(coordinates)

# Algorithm application
tour, max_distance = find_approx_min_bottleneck_hamiltonian_cycle(G, 0)

# Calculate the total travel cost
total_travel_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Create output
output = {
    'Tour': tour,
    'Total travel cost': total_travel_cost,
    'Maximum distance between consecutive cities': max_distance
}

# Print the outputs
print(f"Tour: {output['Tour']}")
print(f"Total travel cost: {output['Total travel cost']:.2f}")
print(f"Maximum distance between consecutive cities: {output['Maximum distance between consecutive cities']:.2f}")