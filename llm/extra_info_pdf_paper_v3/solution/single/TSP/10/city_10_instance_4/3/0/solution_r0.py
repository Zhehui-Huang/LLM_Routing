import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph with distances
def complete_graph(cities):
    graph = {}
    for c1, c2 in combinations(cities.keys(), 2):
        dist = distance(c1, c2)
        graph[(c1, c2)] = dist
        graph[(c2, c1)] = dist
    return graph

# Functions to determine the Minimum Spanning Tree using Kruskal's algorithm
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(nodes, edges):
    parent = {}
    rank = {}
    for node in nodes:
        parent[node] = node
        rank[node] = 0
    mst = []
    edges = sorted(edges, key=lambda item: item[2])
    for edge in edges:
        u, v, w = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append(edge)
    return mst

# Create dictionary of nodes for creating the complete graph
nodes = list(cities.keys())

# Generate all edges with distances
edges = [(u, v, distance(u, v)) for u, v in combinations(nodes, 2)]

# Generate the minimum spanning tree using Kruskal's algorithm
mst = kruskal(nodes, edges)

# Double tree algorithm to approximate TSP
def double_tree_tsp(nodes, mst_edges, graph):
    # Create adjacency list from MST edges
    adj_list = {node: [] for node in nodes}
    for u, v, w in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Use TSP double tree approximation starting from the depot (node 0)
    # Perform DFS to get a pre-order traversal
    def dfs(v, parent):
        tour.append(v)
        for child in adj_list[v]:
            if child != parent:
                dfs(child, v)
                tour.append(v)

    tour = []
    dfs(0, -1)

    # Remove duplicate visits (make the tour a proper Hamiltonian circuit)
    visited = set()
    final_tour = []
    for city in tour:
        if city not in visited:
            final_tour.append(city)
            visited.add(city)
    final_tour.append(0)  # Returning to the depot city

    # Calculate the total travel cost of the tour
    total_cost = sum(graph[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    return final_tour, total_cost

# Prepare graph for TSP approximation
graph = complete_graph(cities)

# Calculate the approximated TSP tour and total cost using the double tree method
tour, total_travel_cost = double_tree_tsp(nodes, mst, graph)

# Output results as required
output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_travel_text}"
print(output_tour)
print(output_total_text)