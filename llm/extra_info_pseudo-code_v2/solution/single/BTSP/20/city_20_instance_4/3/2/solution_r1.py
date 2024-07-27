import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (26, 60),  # City 0:  Depot
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Initial graph
n = len(cities)
G = nx.Graph()
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=dist)

# Initialize biconnected component
def find_bottleneck_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for k in range(1, len(edges_sorted) + 1):
        temp_graph = nx.Graph()
        temp_graph.add_edges_from(edges_sorted[:k])
        if nx.is_biconnected(temp_graph):
            return temp_graph
    return None

subgraph = find_bottleneck_biconnected_subgraph(G)

# Find a cycle in the biconnected graph
cycle_base = list(nx.approximation.traveling_salesman_problem(subgraph, cycle=True))
cycle_base.append(cycle_base[0])

# Calculate costs
total_cost = sum(euclidean_distance(cities[cycle_base[i]], cities[cycle_base[i+1]]) for i in range(len(cycle_base)-1))
max_distance = max(euclidean_distance(cities[cycle_base[i]], cities[cycle_base[i+1]]) for i in range(len(cycle_base)-1))

print(f"Tour: {cycle_base}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")