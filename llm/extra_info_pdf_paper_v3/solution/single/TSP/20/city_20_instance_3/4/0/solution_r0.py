import math
from itertools import combinations
from heapq import *
from collections import defaultdict, deque

# Cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Number of cities
n = len(cities)

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create a complete graph with distances between all cities
edges = []
for c1, c2 in combinations(cities.keys(), 2):
    dist = euclidean_distance(c1, c2)
    edges.append((dist, c1, c2))

# Helper function to find Kruskal's MST
def kruskal_mst(edges, num_nodes):
    edges.sort()  # Sort edges by ascending edge weight
    parent = list(range(num_nodes))  # Union-find parent array
    rank = [0] * num_nodes  # Union-find rank array
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # Building the MST
    mst = []
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((dist, u, v))

    return mst

# Get MST via Kruskal's algorithm
mst = kruskal_mst(edges, n)

# Find all nodes with odd degree in MST
degree = defaultdict(int)
for _, u, v in mst:
    degree[u] += 1
    degree[v] += 1

odd_degree_nodes = [node for node in degree if degree[node] % 2 != 0]

# Compute minimum cost perfect matching amongst the odd degree nodes
def min_cost_perfect_matching(nodes):
    num_nodes = len(nodes)
    edges_odd = []
    index = {node: i for i, node in enumerate(nodes)}
    
    # Build the potential matching graph
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            n1, n2 = nodes[i], nodes[j]
            dist = euclidean_distance(n1, n2)
            edges_odd.append((dist, n1, n2))
    
    # Kruskal's algorithm to find the minimum cost matching, attempting a full coverage every pair.
    match_mst = kruskal_mst(edges_odd, num_nodes)
    min_matching = []
    node_covered = set()
    
    for cost, u, v in match_mst:
        if u not in node_covered and v not in node_covered:
            min_matching.append((cost, u, v))
            node_covered.add(u)
            node_covered.add(v)
            if len(node_covered) == num_nodes:
                break

    return min_matching

matching = min_cost_perfect_matching(odd_degree_nodes)

# Combine MST and matching
mst.extend(matching)

# Create graph from mst + matching
graph = defaultdict(list)
for cost, u, v in mst:
    graph[u].append((cost, v))
    graph[v].append((cost, u))

# Find an Eulerian circuit from this graph
def find_eulerian_tour(graph, start_node):
    tour = []
    stack = [start_node]
    current_node = start_node
    
    while stack:
        if graph[current_node]:
            next_node = graph[current_node].pop()[1]
            stack.append(current_node)
            current_node = next_node
        else:
            tour.append(current_node)
            current_node = stack.pop()
    
    return tour[::-1]

eulerian_tour = find_eulerian_tour(graph, 0)

# Convert Eulerian to Hamiltonian circuit
def convert_to_hamiltonian(eulerian_tour):
    visited = set()
    hamiltonian_tour = []
    for node in eulerian_tour:
        if node not in visited:
            hamiltonian_tour.append(node)
            visited.add(node)
    hamiltonian_tour.append(hamiltonian_tour[0])
    return hamiltonian_tour

hamiltonian_tour = convert_to_hamiltonian(eulerian_tour)

# Calculate the total cost of the hamiltonian tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

total_cost = calculate_tour_cost(hamiltonian_tour)

print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_cost:.2f}")