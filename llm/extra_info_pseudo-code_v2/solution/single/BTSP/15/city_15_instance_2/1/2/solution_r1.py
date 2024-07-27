import math
import networkx as nx

# Define city coordinates
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

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Build a graph
def build_graph():
    G = nx.Graph()
    for src in cities:
        for dest in cities:
            if src != dest:
                G.add_edge(src, dest, weight=euclidean_distance(src, dest))
    return G

# Find the BTSP tour using a heuristic approach
def find_btsp_tour(G):
    # Create MST + 1 to ensure it is bi-connected
    mst_edges = list(nx.minimum_spanning_edges(G, data=True))
    G_mst = nx.Graph()
    G_mst.add_edges_from(mst_edges)
    
    # Adding one more edge to ensure biconnected
    non_mst_edges = [edge for edge in G.edges(data=True) if edge not in mst_edges]
    non_mst_edges.sort(key=lambda x: x[2]['weight'])  # Sort for minimal added weight
    for edge in non_mst_edges:
        G_mst.add_edge(*edge[:2], weight=edge[2]['weight'])
        if nx.is_biconnected(G_mst):
            break
    
    # Find the Hamiltonian cycle in this biconnected graph
    cycle = nx.approximation.traveling_salesman_problem(G_mst, cycle=True, weight='weight')
    
    # Calculate the tour details
    max_dist = 0
    total_dist = 0
    for i in range(len(cycle)-1):
        dist = G[cycle[i]][cycle[i+1]]['weight']
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    
    # Include the return to the start
    back_home_dist = G[cycle[-1]][cycle[0]]['weight']
    total_dist += back_home_dist
    max_dist = max(max_dist, back_home_dist)
    
    cycle.append(clean_cycle[0])  # make it a full loop ending at the starting point
    return cycle, total_dist, max_dist

# Main
G = build_graph()
tour, total_travel_cost, max_consecutive_distance = find_btsp_tour(G)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_radius:.2f}")