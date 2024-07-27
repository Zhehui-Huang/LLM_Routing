import math
import networkx as nx

# Coordinates for each city indexed from 0 to 9
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(cityA, cityB):
    return math.sqrt((cityA[0] - cityB[0])**2 + (cityA[1] - cityB[1])**2)

# Create a weighted complete graph G(V, E)
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Apply Algorithm BB to obtain G(V, E_BB) using networkx
# Sort edges by weight for the initial step
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
E_BB = set()
subgraph = nx.Graph()

# Build the Bottleneck-optimal biconnected subgraph G(V, E_BB)
for edge in edges_sorted:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(subgraph):
        E_BB.add(edge)
        break
    E_BB.add(edge)

# Finding the maximal weight in the biconnected subgraph
c_BB = max([data['weight'] for (u, v, data) in E_BB])

# Finding an approximate optimal tour using the subgraph
# We convert our graph into a square graph (close approximation)
square_graph = nx.Graph()
for edge in E_BB:
    for edge2 in E_BB:
        if edge != edge2 and (edge[1] == edge2[0] or edge[0] == edge2[1]):
            square_graph.add_edge(edge[0], edge2[1], weight=euclidean_distance(cities[edge[0]], cities[edge2[1]]))

# Find Hamiltonian circuit using approximation from biconnected subgraph
tour = list(nx.approximation.traveling_salesman_problem(square_graph, weight='weight', cycle=True))
tour.append(tour[0])

# Calculating total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Outputting results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max.messaging:.2f}")