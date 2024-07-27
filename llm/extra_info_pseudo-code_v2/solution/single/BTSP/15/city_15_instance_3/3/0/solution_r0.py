import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities' coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the distances between each pair of cities
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=distances[i][j])

# Step 1: Bottleneck-optimal Biconnected Subgraph
def algorithm_BB(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = nx.Graph()
    BB.add_nodes_from(G.nodes())

    for edge in edges_sorted:
        BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(BB):
            return BB, max([d['weight'] for u, v, d in BB.edges(data=True)])

# Obtain the bottleneck-optimal biconnected subgraph
BB, c_BB = algorithm_BB(G)

# Step 2: Tour Identification
def find_approximate_tour(BB):
    # Create square of the bottleneck biconnected subgraph
    GG = nx.Graph()
    GG.add_nodes_from(BB.nodes())
    for u in BB.nodes():
        for v in BB.nodes():
            if u != v:
                path_length = nx.shortest_path_length(BB, source=u, target=v, weight='weight', method='dijkstra')
                GG.add_edge(u, v, weight=path_length)
    
    # Find a Hamiltonian cycle (approx.)
    cycle = nx.approximation.traveling_salesman_problem(GG, cycle=True, weight='weight')
    return cycle, max(distances[cycle[i]][cycle[i+1]] for i in range(len(cycle)-1))

cycle, max_distance = find_approximate_tour(BB)

# Calculate the total travel cost
total_cost = sum(distances[cycle[i]][cycle[(i+1) % len(cycle)]] for i in range(len(cycle)))

# Output the results
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")