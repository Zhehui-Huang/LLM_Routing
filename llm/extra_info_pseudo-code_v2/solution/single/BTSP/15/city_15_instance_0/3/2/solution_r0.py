import math
import networkx as nx
import matplotlib.pyplot as plt

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create weighted complete graph G(V, E)
def create_graph():
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

G = create_graph()

# Sort edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2][',! ')

def find_bottleneck_biconnected():
    """Using a heuristic to construct a bottleneck biconnected subgraph."""
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())
    
    for u, v, d in edges_sorted:
        G_BB.add_edge(u, v, weight=d['weight'])
        if nx.is_biconnected(G_BB):
            return G_BB
    return None

def find_bottleneck_tour(G_BB):
    """Find an approximate optimal tour in the squared graph."""
    # Generating the squared graph
    G_square = nx.Graph()
    G_square.add_nodes_from(G_BB.nodes())
    for u in G_BB.nodes:
        neighbors = list(G_BB.neighbors(u))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                n1, n2 = neighbors[i], neighbors[j]
                w = max(G_BB[u][n1]['weight'], G_BB[u][n2]['weight'])
                if G_square.has_edge(n1, n2):
                    if G_square[n1][n2]['weight'] > w:
                        G_square[n1][n2]['weight'] = w
                else:
                    G_square.add_edge(n1, n2, weight=w)
    
    # Finding a Hamiltonian path
    tsp_tour = nx.approximation.traveling_salesman_problem(G_square, cycle=True, weight='weight')
    return tsp_tour

# Execute the functions
G_BB = find_bottleneck_biconnected()
tour = find_bottleneck_tour(G_BB)
max_distance = max([G_BB[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1)])

# Calculate the total travel cost
total_cost = sum([G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1)])

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")

# Plotting
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()