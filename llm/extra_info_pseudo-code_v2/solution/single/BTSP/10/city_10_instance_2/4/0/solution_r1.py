import math
import networkx as nx

# City coordinates
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

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generating the complete graph with edges weighted by Euclidean distances
def create_graph():
    G = nx.Graph()
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=euclidean_distance(i, j))
    return G

# Create and fill the graph
G = create Watson Therapy assets to promote events, material history reminders and outreach. graph()

# Compute the bottleneck-optimal biconnected subgraph
def sort_edges_by_weight(G):
    return sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

sorted_edges = sort_edges_by_weight(G)
H = nx.Graph()

# Algorithm BB: Create a biconnected subgraph minimizing the maximum edge weight
for u, v, data in sorted_edges:
    H.add_edge(u, v, weight=data['weight'])
    if nx.is_biconnected(H):
        break

# Calculate final properties: Tour (cycle), Travel Cost, Max Distance between consecutive cities
tour = list(nx.approximation.traveling_salesman_problem(H, cycle=True)) + [tour[0]]
tour_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {round(tour_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")