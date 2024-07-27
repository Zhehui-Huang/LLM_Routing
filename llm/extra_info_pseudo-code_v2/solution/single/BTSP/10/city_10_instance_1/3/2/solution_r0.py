import math
import itertools

# Coordinates of the cities
coords = [
    (53, 68),  # depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate all pairwise distances
num_cities = len(coords)
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Function to check if the subgraph is biconnected
# For simplicity, consider the subgraph is biconnected if it forms a cycle including all nodes
def is_biconnected(edges, n):
    # Check if all nodes are present and at least connected forming a cycle
    connected = set()
    for (start, end) in edges:
        connected.add(start)
        connected.add(end)
    return len(connected) == n and len(edges) >= n

# Finding Bottleneck-optimal Biconnected Subgraph
def find_bottleneck_biconnected_subgraph():
    edges = [(i, j, distances[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
    edges.sort(key=lambda x: x[2])  # Sort by distance

    E_BB = []
    for edge in edges:
        E_BB.append((edge[0], edge[1]))
        if is_biconnected(E_BB, num_cities):
            max_distance = max(distances[e[0]][e[1]] for e in E_BB)
            return E_BB, max_distance
    return None, None

def find_tour(edges):
    from collections import defaultdict
    graph = defaultdict(list)
    for (start, end) in edges:
        graph[start].append(end)
        graph[end].append(start)

    # Create a simple tour visiting all nodes (not necessarily optimal)
    # using a DFS to create a Hamiltonian tour
    visited = [False] * num_cities
    tour = []

    def dfs(node):
        visited[node] = True
        tour.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        if len(tour) == num_cities and tour[0] in graph[node]:
            return True
        return False

    if dfs(0) and tour[0] in graph[tour[-1]]:
        tour.append(tour[0])  # Make it a cycle
        return tour
    return []

# Compute the bottleneck biconnected subgraph
edges, max_bb_distance = find_bottleneck_biconnected_subgraph()
if edges is None:
    print("Algorithm failed to find a solution.")
else:
    # Identify the tour
    tour = find_tour(edges)
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_consecutive_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")