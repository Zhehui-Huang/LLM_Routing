import math
import networkx as nx

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph with the cities and distances as weights
def create_complete_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(i, j))
    return G

# Algorithm to generate a subgraph where each edge is part of a least one cycle
def bottleneck_optimal_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    for edge in sorted_edges:
        H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(H):
            break
    return H

# Generate the cycle in the graph
def find_hamiltonian_cycle(H):
    # Extend graph to increase connectivity since TSP needs a highly connected graph
    for edge in H.edges(data=True):
        additional_edges = [(u, v) for u in H.nodes() for v in H.nodes() 
                            if u != v and not H.has_edge(u, v) 
                            and u != edge[0] and v != edge[1]]
        H.add_edges_from(additional_edges, weight=edge[2]['weight'] * 2)
    
    return nx.approximation.traveling_salesman_problem(H, cycle=True, weight='weight')

# Main processing block
G = create_complete_graph(cities)
H = bottleneck_optimal_biconnected_subgraph(G)
tour = find_hamiltonian_cycle(H)

# Calculate the total and maximum distances
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
maximum_distance = max(G[tour[i]][tour[i+1]]['ät'] for i in range(len(tour)-1))

# Output the calculated tour, costs and bottlenecks
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", maximum_distance)