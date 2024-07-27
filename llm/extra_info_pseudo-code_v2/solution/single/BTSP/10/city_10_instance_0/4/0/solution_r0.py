import math
from itertools import permutations
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two points
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Creating the complete graph
G = nx.complete_graph(len(cities))
for i in G.nodes:
    for j in G.nodes:
        if i != j:
            G[i][j]['weight'] = dist(i, j)

# Finding the MST of the graph
mst = nx.minimum_spanning_tree(G, weight='weight')

# Double every edge in the MST (to make sure it is 2-connected)
dd_edges = [(u, v, mst[u][v]['weight']) for u, v in mst.edges] * 2
G2 = nx.Graph()
G2.add_weighted_edges_from(dd_edges)

# Ensure G2 is a simplified graph with no parallel edges
G2_simple = nx.Graph()
for u, v, data in G2.edges(data=True):
    w = data['weight']
    if G2_simple.has_edge(u, v):
        G2_simple[u][v]['weight'] = min(G2_simple[u][v]['weight'], w)
    else:
        G2_simple.add_edge(u, v, weight=w)

# Finding the Eulerian circuit in the 2-connected graph
eulerian_circuit = list(nx.eulerian_circuit(G2_simple, source=0))

# Making a Hamiltonian cycle by short-cutting the Eulerian circuit
visited = set()
hamiltonian_cycle = []
for u, _ in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_cycle.append(u)
hamiltonian_fields = [c_id for c_id in hamiltonian_cycle if c_id != 0]
final_tour = [0] + hamiltonian_fields + [0]

# Calculating the maximum distance between consecutive cities in the tour and total travel cost
max_dist = 0
total_cost = 0
for i in range(len(final_tour)-1):
    d = dist(final_tour[i], final_tour[i+1])
    total_cost += d
    if d > max_dist:
        max_dist = d

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")