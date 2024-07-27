import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def build_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def biconnect_graph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for u, v, data in edges_sorted:
        G[u][v]['selected'] = True
        if nx.is_biconnected(G.subgraph([u, v for u, v in G.edges if G[u][v].get('selected')])):
            max_weight = data['weight']
            break
        else:
            G[u][v]['selected'] = False
    return max_weight

def find_tour(G, max_weight):
    subgraph_edges = [(u, v) for u, v in G.edges if G[u][v].get('selected')]
    subgraph = G.edge_subgraph(subgraph_edges).copy()
    square = nx.power(subgraph, 2)
    tour = list(nx.approximation.traveling_salesman_problem(square, cycle=True))
    return tour, max_weight

def calculate_cost_metrics(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

cities = [
    (53, 68), 
    (75, 11), 
    (91, 95), 
    (22, 80), 
    (18, 63), 
    (54, 91), 
    (70, 14), 
    (97, 44), 
    (17, 69), 
    (95, 89)
]

G = build_graph(cities)
max_weight = biconnect_graph(G)
tour, max_weight = find_tour(G, max_weight)
tour.append(tour[0])
total_cost, max_distance = calculate_cost_metrics(cities, tour)

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(output)