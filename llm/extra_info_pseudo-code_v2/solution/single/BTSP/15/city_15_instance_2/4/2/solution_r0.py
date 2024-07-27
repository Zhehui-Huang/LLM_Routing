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
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create weighted complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Algorithm BB
def algorithm_bb(graph):
    E_BB = []
    biconnected_components = []
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    while not nx.is_biconnected(graph.edge_subgraph(E_BB)):
        E_BB.append(sorted_edges.pop(0))
        # Need to include all edges in the subgraph extraction
        graph_bb = graph.edge_subgraph([e[:2] for e in E_BB])
        biconnected_components = list(nx.biconnected_components(graph_bb))

    return graph_bb

# Step 1: Bottleneck-optimal Biconnected Subgraph
graph_bb = algorithm_bb(G)

# Step 2: Identify an approximate optimal tour
def identify_tour(graph_bb):
    for component in nx.connected_components(graph_bb):
        if 0 in component:
            subgraph = graph_bb.subgraph(component)
            try:
                tour = nx.approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight')
                break
            except:
                continue
    return tour

tour = identify_tour(graph_bb)
max_dist = max([graph_bb[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:])])
total_cost = sum([graph_bb[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:])])

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")