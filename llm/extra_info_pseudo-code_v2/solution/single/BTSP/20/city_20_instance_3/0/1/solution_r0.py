import math
from itertools import combinations

# Definition of cities coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Step 0: Calculate the Euclidean distance between each pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph
edges = {(i, j): euclidean_distance(cities[i], cities[j]) for i, j in combinations(range(len(cities)), 2)}

# Step 0 (Initialization): 
# Sort edges by weight
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Algorithm BB
def find_biconnected_subgraph(V, sorted_edges):
    # Initialize sets and the representative graph structure
    parent = {i: None for i in range(V)}
    E_BB = []

    def find_root(v, parent):
        if parent[v] is None:
            return v
        else:
            return find_root(parent[v], parent)

    for ((u, v), weight) in sorted_indices:
        # Union-find structure to detect cycles
        root_u = find_root(u, parent)
        root_v = find_root(v, parent)

        if root_u != root_v:
            E_BB.append((u, v, weight))
            parent[root_v] = root_u

        if len(E_BB) == V - 1:
            break

    return E_BB

biconnected_edges = find_biconnected_subgraph(len(cities), sorted_edges)

# Create a dictionary of edges for easier check
biconnected_graph = {i: [] for i in range(len(cities))}
for u, v, w in biconnected_edges:
    biconnected_graph[u].append((v, w))
    biconnected_graph[v].append((u, w))

# Step 2: Identifying a Tour starting and ending at the depot (city 0)
def find_tour(current_node, n, visited, path):
    if len(path) == n and path[0] == path[-1]:
        return path
    for (next_node, weight) in biconnected_graph.get(current_node, []):
        if next_node not in visited or (len(visited) == n - 1 and next_node == path[0]):
            visited.add(next_node)
            path.append(next_node)
            result = find_tour(next_node, n, visited, path)
            if result:
                return result
            visited.remove(next_node)
            path.pop()
    return None

# Initialize for tour finding
visited = set([0])
tour = find_tour(0, len(cities), visited, [0])

# Compute total cost and maximum distance
if tour:
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("Tour not found.")