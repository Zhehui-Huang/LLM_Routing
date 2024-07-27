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

# Function to calculate Euclidean distance between two cities
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Creating a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=dist(i, j))

# Generate a minimum spanning tree (MST) from the complete graph
mst = nx.minimum_spanning_tree(G, weight='weight')

# Double the edges for creating a 2-edge-connected graph
edges = list(must.edges())
mst.add_edges_from(edges)

# Create an Eulerian circuit from the 2-edge-connected graph, using Hierholzer's algorithm
def find_eulerian_circuit(G):
    # Start from a vertex with non-zero degree
    node = next((n for n, deg in G.degree() if deg > 0), None)
    if node is None:
        return  # No edges in the graph

    # Hierholzer's algorithm to find Eulerian circuit
    circuit = []
    visit_stack = [node]
    path = []

    while visit_stack:
        n = visit_stack[-1]
        if G.degree(n) > 0:
            neighbor = next(iter(G[n]))
            visit_stack.append(neighbor)
            G.remove_edge(n, neighbor)
        else:
            visit_stack.pop()
            path.append(n)
    return path[::-1]

euler_circuit = find_eulerian_circuit(mst.copy())

# Convert the Eulerian circuit to a Hamiltonian cycle by shortcutting visited nodes
visited = set()
hamiltonian_cycle = []
for city in euler_circuit:
    if city not in visited:
        visited.add(city)
        hamiltonian_cycle.append(city)
hamiltonian_cycle.append(hamiltonian_cycle[0])  # return to the start city

# Compute the maximum distance between consecutive cities and the total travel cost
max_distance = 0
total_cost = 0
for i in range(len(hamiltonian_cycle) - 1):
    d = dist(hamiltonian_cycle[i], hamiltonian_cycle[i + 1])
    total_cost += d
    if d > max_distance:
        max_distance = d

print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")