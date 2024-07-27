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
distances = [[euclidean_equal_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Finding Bottleneck-optimal Biconnected Subgraph
def find_bottleneck_biconnected_subgraph():
    edges = [(i, j) for i in range(num_cities) for j in range(i + 1, num_cities)]
    edges.sort(key=lambda x: distances[x[0]][x[1]])  # Sort by distance

    E_BB = []
    for edge in edges:
        E_BB.append(edge)
        if is_biconnected(E_BB, num_cities):
            max_distance = max(distances[e[0]][e[1]] for e in E_BB)
            return E_BB, max_distance
    return None, None

# The DFS function to find a cycle including all nodes
def find_tour(edges):
    from collections import defaultdict
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    # Traverse using DFS to find a Hamiltonian cycle
    tour = []
    visited = [False] * num_cities
    def dfs(node):
        visited[node] = True
        tour.append(node)
        if len(tour) == num_cities:
            if tour[0] in graph[node]:  # check if we can return to origin
                tour.append(tour[0])
                return True
            else:
                return False
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        tour.pop()
        visited[node] = False
        return False

    dfs(0)
    return tour

edges, max_bb_distance = find_bottleneck_biconnected_subgraph()
if edges is not None:
    tour = find_tour(edges)
    if tour and tour[-1] == tour[0] and len(tour) == num_cities + 1:
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        max_consecutive_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
    else:
        print("Failed to find a valid tour.")
else:
    print("Failed to find a biconnected subgraph or calculate its properties.")