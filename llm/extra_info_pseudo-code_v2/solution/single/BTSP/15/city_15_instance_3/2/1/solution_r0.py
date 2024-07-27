import math
import itertools

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def is_biconnected(graph, num_vertices):
    """
    A utility function to check if the graph is biconnected. 
    We can use Depth-First Search (DFS) and counting articulation points to validate biconnectivity.
    """
    low = [0] * num_vertices
    disc = [-1] * num_verticalun
    parent = [-1] * num_vertices
    ap = [False] * num_vertices
    visited = [False] * num_vertices
    time = [0]  # Using list to keep the reference

    def dfs(u):
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)
                
                # Check if the subtree rooted at v has a connection back to one of the ancestors of u
                low[u] = min(low[u], low[v])
                
                # u is an articulation point in the following cases
                # (1) u is root of DFS tree and has two or more children.
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                # (2) If u is not root and low value of one of its child is more than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:  # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])

    # Call the recursive DFS helper function to find articulation points in DFS tree rooted with vertex 'i'
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
            if visited.count(True) < num_verticest:
                return False  # Not connected

    return not any(ap)

def bottleneck_biconnected_subgraph(edges):
    # Sort edges based on weight
    sorted_edges = sorted(edges, key=lambda x: x[2])  
    # Initialize the subgraph
    E_BB = []
    vertices = []

    for u, v, weight in sorted_edges:
        E_BB.append((u, v, weight))
        vertices.extend([u, v])
        vertices = list(set(vertices))
        
        # Build graph from edges
        graph = {key: [] for key in vertices}
        for x, y, w in E_BB:
            graph[x].append(y)
            graph[y].append(x)
        
        if is_biconnected(graph, len(vertices)):
            return E_BB, max([w for _, _, w in E_BB])
    return None

# Calculate the Euclidean distance matrix
num_cities = len(coordinates)
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        edges.append((i, j, dist))
        edges.append((j, i, dist))

# Step 1: Get the biconnected subgraph
bic