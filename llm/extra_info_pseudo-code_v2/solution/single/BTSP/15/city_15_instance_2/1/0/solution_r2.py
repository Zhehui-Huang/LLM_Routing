import math
import networkx as nx

# Define coordinates of cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a graph with vertices as cities and edges as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Find a minimum spanning tree of G
mst = nx.minimum_spanning_tree(G)

# Duplicate edges to make it possible to find a eulerian circuit
H = nx.Graph()
for (u, v, wt) in mst.edges(data=True):
    H.add_edge(u, v, weight=wt['weight'])
    H.add_edge(u, v, weight=wt['weight'])  # this duplicates the edges

# Find a eulerian circuit on this new graph
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Create a Hamiltonian path from the Eulerian circuit by short-circuiting any repeated vertices
path = []
visited = set()
for (u, v) in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(0)  # end at the start point

# Calculate the maximum distance and total cost
max_distance = max(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
total_distance = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")