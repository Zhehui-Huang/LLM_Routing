import math
from itertools import combinations
from networkx import Graph, is_biconnected

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (26, 60),  # City 0:  Depot
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 74),  # City 18
    (14, 89)   # City 19
]

# Initialize graph and edge list
G = Graph()
edges_with_weight = []
n = len(cilities)

for i in range(n):
    G.add_node(i)
    for j in range(i + 1, n):
        distance = euclidean_distance(cities[i], cities[j])
        edges_with_weight.append((i, j, distance))
        G.add_edge(i, j, weight=distance)

# Sort edges by weight
edges_with_weight.sort(key=lambda x: x[2])

# Make graph biconnected
G_BB = Graph()
for i in range(n):
    G_BB.add_node(i)

E_BB = []
for edge in edges_with_weight:
    G_BB.add_edge(edge[0], edge[1], weight=edge[2])
    E_BB.append((edge[0], edge[1], edge[2]))
    if is_biconnected(G_BB):
        break

# Find Hamiltonian cycle in the biconnected subgraph's square
def find_hamiltonian_cycle(G):
    path = []
    def visit(u):
        path.append(u)
        if len(path) == len(G):
            if path[0] in G[path[-1]]:
                return True
            path.pop()
            return False
        seen.add(u)
        for v in G[u]:
            if v in seen:
                continue
            if visit(v):
                return True
        seen.remove(u)
        path.pop()
        return False

    for start_node in G.nodes():
        seen = set()
        if visit(start_node):
            path.append(path[0])
            return path
    return []

# Assume the Biconnected subgraph is small enough
H_cycle = find_hamiltonian_cycle(G_BB)

# Calculate the tour details
tour = H_cycle
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")