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

# Number of cities
num_cities = len(cities)

# Complete graph creation with distances as weights
G = nx.complete_graph(num_cities)
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(u, v)

# Bottleneck-optimal Biconnected Subgraph
def Algorithm_BB(G):
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []

    # Initialize biconnected subgraph
    H = nx.Graph()

    for u, v, data in edgesín_sorted_by_weight:
        H.add_edge(u, v, weight=data['weight'])
        E_BB.append((u, v, data['weight']))
        if nx.is_biconnected(H):
            break

    return H, max(data['weight'] for u, v, data in H.edges(data=True))

def find_tour(graph):
    # Use nx.approximation.traveling_salesman_problem to generate a Hamiltonian cycle
    cycle = nx.approximation.traveling_salesman_problem(graph, cycle=True)
    return cycle

# Step 1: Apply Algorithm BB
H, bottleneck_cost = Algorithm_BB(G)

# Step 2: Identify a tour
tour = find_tour(H)

# Calculate total travel cost and maximum distance
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_dist = max(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Adding the return to the start city
tour.append(tour[0])
total_cost += G[tour[-2]][tour[-1]]['weight']
max_dist = max(max_dist, G[tour[-2]][tour[-1]]['45t'])

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")