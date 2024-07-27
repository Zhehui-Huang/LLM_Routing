import math
import sys
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Compute Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Step 0: Build complete graph with edge weights as distances
def build_complete_graph():
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=distance(i, j))
    return G

# Step 1: Algorithm BB to obtain a bottleneck-optimal biconnected subgraph
def algorithm_bb(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = nx.Graph()
    BB.add_nodes_from(G.nodes())
    
    for u, v, data in edges_sorted:
        BB.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(BB):
            break  # Stop once the graph is biconnected
    
    return BB

# Step 2: Tour identification
def find_tour(G):
    best_tour = None
    lowest_bottleneck = float('inf')

    for cycle in nx.simple_cycles(nx.power(G, 2)):
        if len(cycle) == len(G.nodes()) and cycle[0] == cycle[-1]:  # Only consider cycles that are Hamiltonian
            max_edge_weight = max([G[u][v]['weight'] for u, v in zip(cycle, cycle[1:] + [cycle[0]])])
            if max_edge_weight < lowest_bottleneck:
                lowest_bottleneck = max_edge_weight
                best_tour = cycle
    
    return best_tour, lowest_bottleneck

# Main function to perform steps
def main():
    G = build_complete_graph()
    BB = algorithm_bb(G)
    tour, max_dist = find_tour(BB)

    # Calculate total travel cost
    total_cost = sum([distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)])
    
    # Output
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)

if __name__ == "__main__":
    main()