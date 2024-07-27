import math
from itertools import permutations

# Coordinates of cities (city index: (x, y))
coordinates = {
    0: (16, 90), 
    1: (43, 99), 
    2: (80, 21), 
    3: (86, 92), 
    4: (54, 93), 
    5: (34, 73), 
    6: (6, 61), 
    7: (86, 69), 
    8: (30, 50), 
    9: (35, 73), 
    10: (42, 64), 
    11: (64, 30), 
    12: (70, 95), 
    13: (29, 64), 
    14: (32, 79)
}

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Generate all pairwise distances
num_cities = len(coordinates)
distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Sorting edges by weight
edges = sorted(distances.items(), key=lambda item: item[1])

def is_biconnected(graph, num_vertices):
    """
    Cheapest way to check for biconnected in such small graph is by ensuring
    there's no articulation point. For high number of cities, more efficient algorithms should be used.
    """
    def dfs(v, discovery, low, parent, ap):
        nonlocal time
        # Count of children in DFS Tree
        children = 0
        # Mark the current node as visited
        visited[v] = True

        # Initialize discovery time and low value
        discovery[v] = low[v] = time
        time += 1

        # Go through all vertices adjacent to this
        for to in graph[v]:
            if not visited[to]: # to is not visited
                parent[to] = v
                children += 1
                dfs(to, discovery, low, parent, ap)

                # Check if the subtree rooted at 'to' has a connection
                # back to one of the ancestors of 'v'
                low[v] = min(low[v], low[to])

                # (1) v is root of DFS tree and has two or more children.
                # (2) If v is not root and low value of one of its child is more
                if parent[v] == -1 and children > 1 or parent[v] != -1 and low[to] >= discovery[v]:
                    ap[v] = True
            elif to != parent[v]:  # Update low value of 'v' for parent function calls.
                low[v] = min(low[v], discovery[to])

    visited = [False] * num_vertices
    discovery = [float('inf')] * num_space_vertices
    low = [float('inf')] * num_vertices
    parent = [-1] * num_vertices
    ap = [False] * num_vertices  # To store articulation points
    time = 0

    # Call the recursive helper function to find articulation points
    # in DFS tree rooted with vertex 'i'
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i, discovery, low, parent, ap)
    
    return not any(ap)

# Bottleneck Biconnected Subgraph construction using BB algorithm
def find_bbs():
    # Create an empty graph
    graph = {i: [] for i in range(num_cities)}
    ebbs = []

    for edge, weight in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        ebbs.append((edge, weight))
        if is_biconnected(graph, num_cities):
            return ebbs, graph
        else:
            # Remove the edge if not leading to biconnection
            graph[edge[0]].remove(edge[1])
            graph[edge[1]].remove(edge[0])
            ebbs.pop()

# Finding BBS
ebbs, bbs_graph = find_bbs()

# Identify Hamiltonian cycle in the biconnected subgraph
def find_hamiltonian_path(graph):
    """ Simple brute force approach since num_cities is small; otherwise, use specialized algorithms."""
    for perm in permutations(range(1, num_cities)):
        # Check if the permutation forms a valid cycle with all edges exist in bbs_graph
        valid = True
        path = [0] + list(perm) + [0]
        for i in range(len(path) - 1):
            if path[i+1] not in graph[path[i]]:
                valid = False
                break
        if valid:
            return path

cycle = find_hamiltonian_path(bbs_graph)

# Calculating travel cost and maximum edge cost in the tour
total_travel_cost = sum(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle)-1))
max_distance = max(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle)-1))

print("Tour:", cycle)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)