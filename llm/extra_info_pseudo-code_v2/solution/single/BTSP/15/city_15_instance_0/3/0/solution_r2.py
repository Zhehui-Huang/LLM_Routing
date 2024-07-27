from math import sqrt
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 74), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Function to check if the graph is biconnected
def is_biconnected(graph):
    return nx.is_biconnected(graph)

# Attempt to construct a biconnected graph by adding the shortest edges first
biconnected_subgraph = nx.Graph()
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

for edge in sorted_edges:
    biconnected_subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if is_biconnected(biconnected_subgraph):
        break

# Verify the subgraph is biconnected
if not is_biconnected(biconnected_subgraph):
    print("Failed to construct a biconnected graph.")
else:
    # Find a Hamiltonian cycle in the augmented graph (G^2)
    G2 = nx.power(biconnected_subgraph, 2)
    cycle = list(nx.approximation.traveling_salesman_problem(G2, cycle=True, weight='weight'))
    cycle.append(cycle[0])  # Complete the cycle by connecting back to the start

    # Calculate distances
    total_distance = sum(G[u][v]['weight'] for u, v in zip(capture_head, cycle[1:]))
    max_distance = max(G[u][v]['weight'] for u, v in zip(capture_head, cycle[1:]))
    
    # Output results
    print(f"Tour: {cycle}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")