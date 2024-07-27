import math
import networkx as nx

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Assign weights based on Euclidean distances
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

def is_biconnected(G):
    return nx.is_biconnected(G)

# Implementing the BB Algorithm
def bottleneck_optimal_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    
    for u, v, d in edges_sorted:
        E_BB.add_edge(u, v, weight=d['weight'])
        if is_biconnected(E_BB):
            break
    return E_BB

def find_tour_in_biconnected_subgraph(BB_graph):
    # Create the square of the biconnected subgraph
    G_squared = nx.Graph()
    for u in BB_graph.nodes():
        G_squared.add_node(u)
        paths = nx.single_source_shortest_path(BB_graph, u, cutoff=2)
        for v, path in paths.items():
            if len(path) == 3:  # only add edges that are exactly 2 edges away
                G_squared.add_edge(u, v, weight=BB_graph[path[0]][path[1]]['weight'] + BB_graph[path[1]][path[2]]['weight'])

    # Find a Hamiltonian path in the squared graph
    tour = list(nx.approximation.traveling_salesman_problem(G_squared, cycle=True))
    return tour

# Main execution
BB_graph = bottleneck_optimal_biconnected_subgraph(G)
tour = find_tour_in_biconnected_subgraph(BB_graph)

# Calculate the total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
tour.append(tour[0])  # append the starting node to close the tour
for i in range(len(tour) - 1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")