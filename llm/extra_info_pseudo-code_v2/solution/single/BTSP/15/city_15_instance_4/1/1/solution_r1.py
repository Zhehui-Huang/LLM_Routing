import math
import networkx as nx

def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(city_coords):
    G = nx.Graph()
    n = len(city_coords)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=calc_distance(city_coords[i], city_coords[j]))
    return G

def is_biconnected_subgraph(G):
    return nx.is_biconnected(G)

def bottleneck_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = nx.Graph()
    BB.add_nodes_from(G.nodes())
    for edge in edges_sorted:
        BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if is_biconnected_subgraph(BB):
            return BB
    return None

def solve_btsp(G):
    BB = bottleneck_biconnected_subgraph(G)
    if BB:
        cycle = nx.approximation.greedy_tsp(BB, source=0)
        cycle.append(cycle[0])  # Close the cycle to return to the depot

        total_distance = 0
        max_leg_distance = 0
        for i in range(len(cycle) - 1):
            dist = G[cycle[i]][cycle[i+1]]['weight']
            total_distance += dist
            if dist > max_leg_distance:
                max_leg_dynode = (cycle[i], cycle[i+1])
                max_leg_distance = dist

        return cycle, total_distance, max_leg_distance
    else:
        return None

cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

G = create_complete_graph(cities)
results = solve_btsp(G)

if results:
    tour, total_cost, max_leg_distance = results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_leg_distance)
else:
    print("No biconnected graph could be formed to solve the problem")