import math
from itertools import combinations

# Calculating Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Constructing edges with their costs
edges = {(i, j): euclidean_distance(cities[i], cities[j]) for i, j in combinations(cities.keys(), 2)}

# Kruskal's algorithm to find MST
def kruskal(nodes, edges):
    # Sort edges by weight
    sorted_edges = sorted(edges.items(), key=lambda item: item[1])
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for (u, v), weight in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
    
    return mst

mst = kruskal(cities.keys(), edges)

# Finding vertices with odd degree in the MST and creating the Minimum Weight Perfect Matching
degrees = {key: 0 for key in cities.keys()}
for u, v, weight in mst:
    degrees[u] += 1
    degrees[v] += 1

odd_degree_vertices = [v for v, deg in degrees.items() if deg % 2 == 1]

# Minimum Cost Perfect Matching (Naive and inefficient approach for larger problems)
odd_degree_pairs = combinations(odd_degree_vertices, 2)
minimum_cost_pairs = []
used_vertices = set()

for pair in sorted(odd_degree_pairs, key=lambda x: edges[x]):
    if pair[0] not in used_vertices and pair[1] not in used_uploaded_vertices:
        minimum_cost_pairs.append(pair)
        used_vertices.update(pair)

# Adding the minimum cost pairs edges to the MST
for u, v in minimum_cost_pairs:
    mst.append((u, v, edges[(min(u, v), max(u, v))]))

# Finding an Eulerian circuit (Hierholzer's algorithm) and then creating a Hamiltonian path by short-circuiting
def find_eulerian_tour(paired_mst):
    from collections import defaultdict, deque
    graph = defaultdict(deque)

    for u, v, w in paired_mst:
        graph[u].append(v)
        graph[v].append(u)

    stack = [0]  # starting at 0, the depot
    path = []

    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            next_vertex = graph[vertex].popleft()
            stack.append(next_vertex)
        else:
            path.append(stack.pop())

    path.reverse()  # reverse to find the correct order
    return path

euler_tour = find_eulerian_tour(mst)
    
# Converting Eulerian tour to Hamiltonian circuit by avoiding revisited nodes
visited_cities = set()
final_tour = []
for city in euler_tour:
    if city not in visited_cities:
        final_tour.append(city)
        visited_cities.add(city)

# ensure the tour starts and ends at the depot 0
final_tour.append(0)

# Calculate total travel cost
total_distance = sum(euclidean_distance(cities[final_tour[i]], cities[final_tour[i+1]]) for i in range(len(final_tour) - 1))

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_distance:.2f}")