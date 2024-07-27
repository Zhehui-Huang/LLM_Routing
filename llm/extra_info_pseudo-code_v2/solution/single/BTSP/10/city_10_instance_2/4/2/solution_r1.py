import math
import networkx as nx

def euclidean_distance(coord1, coord2):
    return math.dist(coord1, coord2)

# Input coordinates for the cities
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

# Create a complete graph
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(cities[u], cities[v])

# Sort edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Function to find biconnected subgraph with the smallest max edge weight
def find_bottleneck_biconnected_subgraph(G, edges_sorted):
    H = nx.Graph()
    for edge in edges_sorted:
        H.add_edge(*edge[:2], weight=edge[2]['weight'])
        if nx.is_biconnected(H):
            break
    return H

# Finding the bottleneck optimum biconnected subgraph
H = find_bottleneck_biconnected_subgraph(G, edges_sorted)

# Approximating tour from the subgraph H
def approximate_tour(H):
    # Truncate to nearest Hamiltonian cycle starting from vertex 0
    try:
        cycle = nx.approximation.traveling_salesman_problem(H, cycle=True, weight='weight')
    except:
        cycle = list(nx.find_cycle(H, orientation="original"))
    return cycle

# Approximate tour
tour = approximate_tour(H)

# Calculate max distance and total travel cost from the tour
max_distance = 0
total_travel_cost = 0
for i in range(len(tour) - 1):
    distance = H[tour[i]][tour[i+1]]['weight']
    total_travel_cost += distance
    if distance > max_distance:
        max_distance = distance

# Closing the tour
tour.append(tour[0])
final_distance = H[tour[-2]][tour[-1]]['weight']
total_travel_cost += final_distance
if final_distance > max_distance:
    max_distance = final_distance

# Output the results
print("Tour: ", tour)
print("Total travel cost: ", total_travel_cost)
print("Maximum distance between consecutive cities: ", max_distance)