import math
import networkx as nx
from itertools import permutations

# Data: Coordinates of the cities
locations = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
             (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
             (56, 58), (72, 43), (6, 99)]

def euclidean_distance(loc1, loc2):
    """ Compute Euclidean distance between two points """
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

def create_complete_graph(locations):
    """ Prepare a complete graph with weighted edges based on the locations """
    G = nx.Graph()
    n = len(locations)
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(locations[i], locations[j]))
    return G

def create_biconnected_subgraph(G):
    """ Build a bottleneck-optimal biconnected subgraph using the heuristic algorithm """
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(G.nodes())
    
    for edge in edges_sorted:
        biconnected_subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            break
    
    return biconnected_subgraph

def square_of_graph(bg):
    """ Construct square of biconnected graph where each vertex is joined to neighbors of neighbors """
    s = nx.Graph()
    s.add_nodes_from(bg.nodes())
    for v in bg:
        neighbors = list(bg[v])
        s.add_edges_from((v, w) for w in neighbors)
        for u in neighbors:
            s.add_edges_from((v, z) for z in bg[u] if z != v)
    return s

def find_approximate_tour(G):
    """ Attempt to find an approximate optimal BTSP tour using the algorithms provided """
    b_graph = create_biconnected_subgraph(G)
    s_graph = square_of_graph(b_graph)
    
    # Find a short cycle visiting all vertices (a rough approximation of the Hamiltonian cycle problem)
    min_tour_length = float('inf')
    best_tour = None
    for cycle in permutations(s_graph.nodes()):
        if len(cycle) == s_graph.number_of_nodes() and cycle[0] == cycle[-1]:
            length = sum(s_graph[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]))
            if length < min_tour_length:
                min_tour_length = length
                best_tour = cycle
    
    # Return the found tour
    return best_tour, min_tour_length

# Main Execution
G = create_complete_graph(locations)
tour, weight = find_approximate_taur(G)
tour = tour + (tour[0],)  # Close the cycle
tour_distances = [euclidean_distance(locations[tour[i]], locations[tour[i+1]]) for i in range(len(tour)-1)]
max_distance = max(tour_distances)
total_cost = sum(tour_distances)

# Results Output
print("Tour:", list(tour))
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)