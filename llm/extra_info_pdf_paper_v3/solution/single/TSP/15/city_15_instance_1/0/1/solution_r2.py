import math
from collections import defaultdict
from heapq import heappop, heappush

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Prim's algorithm to find the Minimum Spanning Tree (MST)
def minimum_spanning_tree(coords):
    n = len(coords)
    in_mst = [False] * n
    min_edge = [(float('inf'), -1)] * n
    mst_edges = []
    min_edge[0] = (0, 0)
    edges_pq = [(0, 0)]  # (cost, node)

    while edges_pq:
        current_cost, u = heappop(edges_pq)

        if in_mst[u]:
            continue

        in_mst[u] = True
        for v in range(n):
            if not in_mst[v] and coords[u] != coords[v]:
                cost = euclidean_distance(coords[u], coords[v])
                if cost < min_edge[v][0]:
                    min_edge[v] = (cost, u)
                    heappush(edges_pq, (cost, v))

    for cost, u in min_edge:
        if u != -1:
            mst_edges.append((u, min_edge[u][1]))

    return mst_edges

# Build graph from edges
def build_graph(edges, n):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# DFS to find odd degree vertices
def find_odd_vertices(graph, n):
    odd_vertices = []
    for node in range(n):
        if len(graph[node]) % 2 == 1:
            odd_vertices.append(node)
    return odd_vertices

# Greedy Minimum-Cost Perfect Matching
def greedy_minimum_matching(odd_vertices, coords):
    matched = set()
    matching_edges = []
    while odd_vertices:
        v = odd_vertices.pop()
        if v in matched:
            continue
        min_cost, u = min((euclidean_distance(coords[v], coords[u]), u) 
                          for u in odd_vertices if u not in matched)
        matching_edges.append((v, u))
        matched.add(v)
        matched.add(u)
        odd_vertices.remove(u)
    return matching_edges

# Hierholzer's algorithm to find Eulerian circuit
def eulerian_circuit(start, graph):
    stack, path = [start], []
    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            next_vertex = graph[vertex].pop()
            stack.append(next_vertex)
        else:
            path.append(stack.pop())
    return path[::-1]

# Make the tour Hamiltonian by skipping repeated visits
def make_hamiltonian(tour, n):
    visited = set()
    hamiltonian_tour = []
    for city in tour:
        if city not in visited:
            visited.add(city)
            hamiltonian_tour.append(city)
    hamiltonian_tour.append(hamiltonian_tour[0])  # to complete the cycle
    return hamiltonian_tour

# Main TSP function
def christofides_tsp(coords):
    n = len(coords)
    mst_edges = minimum_spanning_tree(coords)
    graph = build_graph(mst_edges, n)
    odd_vertices = find_odd_vertices(graph, n)
    matching_edges = greedy_minimum_matching(odd_vertices, coords)
    euler_graph = build_graph(mst_edges + matching_edges, n)
    euler_tour = eulerian_circuit(0, euler_graph)
    hamiltonian_tour = make_hamiltonian(euler_torder(n)

    # Calculate the total travel cost
    total_cost = sum(euclidean_distance(coords[hamiltonian_tour[i]], coords[hamiltonian_tour[i+1]])
                     for i in range(len(hamiltonian_tour) - 1))
    return hamiltonian_tour, total_cost

coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

tour, cost = christofides_tsp(coords)
print("Tour:", tour)
print("Total travel cost:", cost)