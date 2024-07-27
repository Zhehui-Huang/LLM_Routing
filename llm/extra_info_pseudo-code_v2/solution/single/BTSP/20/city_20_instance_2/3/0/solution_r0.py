import itertools
import math
import networkx as nx

# Cities data:
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99),
    (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Step 0: Create a complete graph with Euclidean distance as edge weights
def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Algorithm BB to achieve a bottleneck-optimal biconnected subgraph
def algorithm_bb(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    for u, v, data in sorted_edges:
        biconnected_subgraph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            break
    return biconnected_sub(Create graph with only the needed edgesect_subgraph

# Identify an approximate optimal tour (Step 2)
def approximate_tour(G_bb):
    T = list(nx.minimum_spanning_tree(G_bb).edges())
    cycle = list(nx.eulerian_circuit(nx.MultiGraph(T), source=0))
    visited = set()
    path = []
    for u, v in cycle:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Complete the cycle
    
    return path

def calculate_tour_cost(path, G):
    total_cost = 0
    max_distance = 0
    for i in range(len(path) - 1):
        distance = G[path[i]][path[i+1]]['weight']
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

G = create_graph(cities)
G_bb = algorithm_bb(G)
tour = approximate_tour(G_bb)
total_cost, max_distance = calculate_tour_cost(tour, G)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")