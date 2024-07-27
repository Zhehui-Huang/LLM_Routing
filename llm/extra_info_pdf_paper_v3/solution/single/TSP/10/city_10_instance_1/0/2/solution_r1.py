import math
from itertools import combinations

# Define coordinates of the cities
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Euclidean distance calculator
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Generate the graph edges with their weights (distances)
edges = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i < j}

# Function to find Minimum-Cost Perfect Matching for vertices of odd degree in the MST
def perfect_matching(odd_vertices, edges):
    from heapq import heappop, heappush
    match_edges = []
    while odd_vertices:
        v = odd_vertices.pop()
        distances = [(edges[min(v, u), max(v, u)], u) for u in odd_vertices]
        min_edge = min(distances, key=lambda x: x[0])
        u = min_edge[1]
        match_edges.append((v, u, min_edge[0]))
        odd_vertices.remove(u)
    return match_edges

# Use Kruskal's Algorithm to find the MST (minimum spanning tree)
def kruskal(nodes, edges):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(n1, n2):
        root1 = find(n1)
        root2 = find(n2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
                    
    mst = []
    for edge in sorted(edges, key=edges.get):
        u, v = edge
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, edges[edge]))
    
    return mst

# Find the Eulerian Tour (Hierholzer's Algorithm)
def eulerian_tour(start, adj_list):
    stack = [start]
    path = []
    while stack:
        while adj_list[stack[-1]]:
            next_city = adj_list[stack[-1]].pop()
            stack.append(next_city)
        path.append(stack.pop())
    return path[::-1]

# Convert Eulerian Tour to Hamiltonian Path (avoid repeated visits)
def make_hamiltonian(euler_tour, start):
    visited = set()
    path = []
    for city in euler_tour:
        if city not in visited or city == start:
            visited.add(city)
            path.append(city)
    return path

# Main computation block
node_list = list(cities.keys())
mst = kruskal(node_list, edges)
degrees = {node: 0 for node in node_list}
for u, v, w in mst:
    degrees[u] += 1
    degrees[v] += 1

adj_list = {node: [] for node in node_list}
for u, v, w in mst:
    adj_list[u].append(v)
    adj_list[v].append(u)

odd_degree_nodes = [node for node, deg in degrees.items() if deg % 2 == 1]
matching = perfect_matching(odd_degree_nodes, edges)
for u, v, w in matching:
    adj_list[u].append(v)
    adj_list[v].append(u)

tour = eulerian_tour(0, adj_list)
hamiltonian_path = make_hamiltonian(tour, 0)
total_distance = sum(edges[min(hamiltonian_path[i], hamiltonian_path[i+1]), max(hamiltonian_path[i], hamiltonian_path[i+1])] for i in range(len(hamiltonian_path)-1))

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_distance:.2f}")