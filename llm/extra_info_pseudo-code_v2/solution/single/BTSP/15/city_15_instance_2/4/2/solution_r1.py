import math
import networkx as nx

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(c1, c2):
    return math.dist(c1, c2)

# Create weighted complete graph G(V, E)
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Algorithm to obtain a bottleneck-optimal biconnected subgraph
def algorithm_bb(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []

    for edge in sorted_edges:
        E_BB.append(edge)
        subgraph = graph.edge_subgraph([e[:2] for e in E_BB])
        if nx.is_biconnected(subgraph):
            break

    return subgraph

# Step 1: Bottleneck-optimal Biconnected Subgraph
graph_bb = algorithm_bb(G)

# Step 2: Tour Identification
def identify_tour(graph_bb):
    # Finding a Hamiltonian cycle starting and ending at the depot city (node 0)
    t = nx.approximation.traveling_salesman_problem(graph_bb, cycle=True, weight='weight', source=0)
    return t

tour = identify_tour(graph_bb)
max_dist = max([euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)])
total_cost = sum([euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)])

# Output the tour, total cost, and maximum distance between consecutive cities
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")