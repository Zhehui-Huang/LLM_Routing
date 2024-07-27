import itertools
import math
from networkx import Graph, biconnected_components

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Create a complete graph with cities and edge weights as Euclidean distances
def create_complete_graph(cities):
    G = Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Algorithm BB to find a bottleneck optimal biconnected subgraph
def algorithm_bb(G):
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = Graph()
    BB.add_nodes_from(G.nodes())
    for u, v, data in edges:
        BB.add_edge(u, v, weight=data['weight'])
        if len(list(biconnected_components(BB))) > 1:
            BB.remove_edge(u, v)
        if BB.number_of_edges() >= len(cities):
            break
    return BB

# Find Hamiltonian cycle in a biconnected subgraph
def find_tour_in_biconnected_graph(BB, start_node):
    path = [start_node]
    visited = set(path)
    current = start_node
    
    while len(path) < BB.number_of_nodes():
        neighbors = [n for n in BB.neighbors(current) if n not in visited]
        if not neighbors:
            break
        next_node = min(neighbors, key=lambda n: BB[current][n]['weight'])
        path.append(next_node)
        visited.add(next_node)
        current = next_node
    
    path.append(start_node)  # Complete the tour by returning to the start
    return path

# Main function to solve the BTSP
def solve_btsp(cities):
    G = create_complete_graph(cities)
    BB = algorithm_bb(G)
    tour = find_tour_in_biconnected_graph(BB, 0)
    total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
    max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
    return tour, total_cost, max_distance

# Output results
tour, total_cost, max_distance = solve_btsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)