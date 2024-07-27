import itertools
import math
import networkx as nx

cities = [
    (3, 26), (85, 72), (67, 0), (50, 99),
    (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def algorithm_bb(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    U = nx.Graph()
    U.add_node(0)

    for u, v, data in sorted_edges:
        U.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(U):
            break
    return U

def find_approximate_tour(G):
    path = []
    try:
        cycle = nx.find_cycle(G, orientation="ignore")  # Attempt to find a cycle assuming graph G is connected and can possibly form a cycle
        path = [node for node, _ in cycle]
        path.append(path[0])  # Ensure return to starting point to complete the tour
    except nx.NetworkXNoCycle:
        path = list(nx.approximation.traveling_salesman_problem(G, weight='weight'))
        path.append(path[0])

    return path

def calculate_tour_metrics(G, tour):
    total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
    max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
    return total_cost, max_distance

G = create_graph(cities)
G_bb = algorithm_bb(G)
tour = find_approximate_tour(G_bb)
total_cost, max_distance = calculate_tour_metrics(G, tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)