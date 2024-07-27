import itertools
import math
from queue import PriorityQueue

# Define city coordinates
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)

# Number of cities
n = len(city_coords)

# Constructing a shortest spanning tree (SST) using Prim's algorithm
def construct_sst():
    in_tree = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    min_edge[0] = 0
    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        _, u = pq.get()
        in_tree[u] = True
        for v in range(n):
            if not in_tree[v] and u != v:
                cost = euclidean_distance(u, v)
                if cost < min_edge[v]:
                    min_edge[v] = cost
                    parent[v] = u
                    pq.put((cost, v))

    edges = []
    for v in range(1, n):
        edges.append((parent[v], v))
    return edges

# Find all vertices with odd degree in the MST to perform a minimum-cost perfect matching on them
def find_odd_vertices(edges):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    odd_vertices = [v for v in range(n) if degree[v] % 2 == 1]
    return odd_vertices

# Greedily find the minimum-cost perfect matching
def min_cost_perfect_matching(odd_vertices):
    matched = [False] * n
    min_matching = []
    while odd_vertices:
        v = odd_vertices.pop()
        if not matched[v]:
            distance = float('inf')
            closest = None
            for u in odd_vertices:
                if not matched[u] and euclidean_distance(u, v) < distance:
                    distance = euclidean_distance(u, v)
                    closest = u
            matched[v] = matched[closest] = True
            min_matching.append((v, closest))
            odd_vertices.remove(closest)
    return min_matching

# Construct final tour using MST edges and the matching
def construct_eulerian_tour(edges, matching):
    adjacency_list = [[] for _ in range(n)]
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    for u, v in matching:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Perform a DFS to get the Eulerian circuit
    tour = []
    stack = [0]
    while stack:
        v = stack[-1]
        if adjacency_list[v]:
            u = adjacency_list[v].pop()
            stack.append(u)
            adjacency_list[u].remove(v)
        else:
            tour.append(stack.pop())
    return tour

def calculate_total_distance(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

# Applying all steps
edges = construct_sst()
odd_vertices = find_odd_vertices(edges)
matching = min_cost_perfect_matching(odd_vertices)
tour = construct_eulerian_tour(edges, matching)

# As we might get a non-Hamiltonian tour (some cities visited more than once),
# we will convert Eulerian tour to Hamiltonian tour by visiting each city once
hamiltonian_tour = []
visited = set()
for city in tour:
    if city not in visited:
        hamiltonian_tour.append(city)
        visited.add(city)

# Ensuring the tour starts and ends at the depot city (0)
if hamiltonian_tour[0] != 0:
    hamiltonian_tour = [0] + hamiltonian_tour
if hamiltonian_tour[-1] != 0:
    hamiltonian_tour.append(0)

total_cost = calculate_total_distance(hamiltonian_tour)

# Output the results in the specified format
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_cost:.2f}")