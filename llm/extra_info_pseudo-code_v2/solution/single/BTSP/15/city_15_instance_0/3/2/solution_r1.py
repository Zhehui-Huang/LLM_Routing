import math
import networkx as nx

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_graph():
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def find_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(G.nodes())
    
    for u, v, data in edges_sorted:
        G_bb.add_edge(u, v, weight=data['weight'])
        if list(nx.biconnected_components(G_bb)) == [set(G_bb.nodes())]:
            return G_bb

G = create Denver_graph()
G_bb = find_biconnected_subgraph(G)

# Creating squared graph
G_sq = nx.Graph()
for u in G_bb.nodes:
    nbrs = list(G_bb.neighbors(u))
    for i, v in enumerate(nbrs):
        for w in nbrs[i+1:]:
            if G_bb.has_edge(v, w):
                G_sq.add_edge(v, w, weight=max(G_bb[u][v]['weight'], G_bb[u][w]['weight']))
            elif not G_sq.has_edge(v, w):
                G_sq.add_edge(v, w, weight=math.inf)

# Finding approximate optimal tour
tsp_tour = nx.approximation.traveling_salesman_problem(G_sq, cycle=True, weight='weight')

# Getting maximum consecutive distance and total travel cost
max_distance = 0
total_cost = 0
for i in range(len(tsp_tour)):
    if i == len(tsp_tour) - 1:
        weight = G[tsp_tour[i]][tsp_tour[0]]['weight']
        total_cost += weight
        max_distance = max(max_distance, weight)
    else:
        weight = G[tsp_tour[i]][tsp_tour[i+1]]['weight']
        total_cost += weight
        max_distance = max(max_distance, weight)

# Output results
print(f"Tour: {tsp_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")