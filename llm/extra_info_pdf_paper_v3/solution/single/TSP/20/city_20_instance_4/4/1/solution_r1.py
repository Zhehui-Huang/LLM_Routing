from math import sqrt
from heapq import heappop, heappush

# Cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distances between all pairs of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Constructing a shortest spanning tree using Prim's algorithm
def prim(distance_matrix):
    n = len(distance_matrix)
    in_tree = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]
    min_edge[0] = (0, None)  # Start from city 0
    mst_edges = []

    for _ in range(n):
        # Find the minimum edge to add
        next_edge = min((edge, idx) for idx, edge in enumerate(min_edge) if not in_tree[idx])
        cost, parent = next_edge
        current = min_edge.index(next_edge)

        in_tree[current] = True
        if parent is not None:
            mst_edges.append((parent, current, min_edge[current][0]))

        for adj in range(n):
            if not in_tree[adj] and distance_matrix[current][adj] < min_edge[adj][0]:
                min_edge[adj] = (distance_matrix[current][adj], current)

    return mst_edges

mst = prim(distances)

# Finding vertices with odd degree in the MST
degrees = [0] * n
for u, v, _ in mst:
    degrees[u] += 1
    degrees[v] += 1

odd_vertices = [idx for idx, deg in enumerate(degrees) if deg % 2 == 1]

# Find minimum-cost perfect matching on odd degree vertices
from itertools import combinations

def perfect_matching(odd_vertices, distance_matrix):
    match = []
    while odd_vertices:
        u = odd_vertices.pop()
        min_cost, v_min = min((distance_matrix[u][v], v) for v in odd_vertices)
        odd_vertices.remove(v_min)
        match.append((u, v_min, min_cost))
    return match

matching = perfect_matching(odd_vertices, distances)
final_edges = mst + matching

# Converting Eulerian trail to a Hamiltonian cycle
from collections import defaultdict

def create_tour(edges, start_vertex):
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    path = []
    stack = [start_vertex]
    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            stack.append(graph[vertex].pop())
            graph[stack[-2]].remove(stack[-1])
        else:
            path.append(stack.pop())
            
    return path[::-1]

tour = create_tour(final_edges, 0)

# Ensure the tour is Hamiltonian and starts and ends at the depot
final_tour = [0]
visited = set([0])
for city in tour:
    if city not in visited:
        visited.add(city)
        final_tour.append(city)
final_tour.append(0)  # Return to the starting city

# Calculate the total travel cost
total_cost = sum(distances[final_tour[i]][final_tour[i + 1]] for i in range(len(final_tour) - 1))

# Output the final tour and total cost
print("Tour:", final_tour)
print("Total travel cost:", total_cost)