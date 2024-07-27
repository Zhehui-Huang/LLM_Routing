import math
import networkx as nx
from itertools import permutations

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

# Create a complete graph with distances as weights
def build_complete_graph():
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=distance(i, j))
    return G

# Tour Identification via Brute Force (small number of cities allows this)
def find_bottleneck_tsp_tour(G):
    best_tour = None
    min_bottleneck = float('inf')
    cities = list(G.nodes())

    for perm in permutations(cities):
        if perm[0] == 0:  # Start at depot
            tour = list(perm) + [0]  # Complete tour back to depot
            max_weight_in_tour = max([G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1)])
        
            if max_weight_in_tour < min_bottleneck:
                min_bottleneck = max_weight_in_tour
                best_tour = tour
    
    total_cost = sum([G[best_tour[i]][best_tour[i+1]]['weight'] for i in range(len(best_tour) - 1)])
    return best_tour, total_cost, min_bottleneck

def main():
    G = build_complete_graph()
    tour, total_cost, max_dist = find_bottleneck_tsp_tour(G)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)

if __name__ == "__main__":
    main()