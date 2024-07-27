import networkx as nx
from itertools import permutations
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define city locations
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Add distances to the graph
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = calculate_distance(cities[u], cities[v])

# Implementing Algorithm BB
def is_biconnected(G):
    return nx.is_biconnected(G)

def algorithm_bb(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    
    for (u, v, data) in sorted_edges:
        E_BB.add_edge(u, v, weight=data['weight'])
        if is_biconnected(E_BB):
            return E_BB

E_BB = algorithm_bb(G)

# Find the approximate optimal tour - Step 2
def find_hamiltonian_cycle(G, start_node):
    """
    A very naive way to find the Hamiltonian cycle - Starting with a heuristic method
    """
    nodes = list(G.nodes())
    min_cycle = None
    min_cost = float('inf')
    for perm in permutations(nodes):
        if perm[0] == start_node:
            valid = True
            max_edge_cost = 0
            cycle_cost = 0
            for i in range(len(perm) - 1):
                if G.has_edge(perm[i], perm[i + 1]):
                    cost = G.edges[perm[i], perm[i + 1]]['weight']
                    cycle_cost += cost
                    max_edge_cost = max(max_edge_cost, cost)
                else:
                    valid = False
                    break
            if valid and G.has_edge(perm[-1], perm[0]):
                cost = G.edges[perm[-1], perm[0]]['weight']
                max_edge_cost = max(max_edge_cost, cost)
                cycle_cost += cost
                if cycle_cost < min_cost:
                    min_cycle = perm + (perm[0],)
                    min_cost = cycle_cost
                    min_max_edge_cost = max_edge_cost
    return min_cycle, min_cost, min_max_edge_cost

tour, cost, max_distance = find_hamiltonian_cycle(E_BB, 0)

# Print the results in the specified format
print("Tour:", list(tour))
print("Total travel cost:", cost)
print("Maximum distance between consecutive cities:", max_distance)