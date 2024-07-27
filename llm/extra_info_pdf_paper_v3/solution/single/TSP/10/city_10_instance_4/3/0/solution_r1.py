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
            mst.append((u, v, w))
    return mst

# Generate the minimum spanning tree using Kruskal's algorithm
nodes = list(cities.keys())
edges = [(u, v, distance(u, v)) for u, v in combinations(nodes, 2)]
mst = kruskal(nodes, edges)

# Double tree algorithm to approximate TSP
def double_tree_tsp(nodes, mst_edges, graph):
    # Create adjacency list from MST edges
    adj_list = {node: [] for node in nodes}
    for u, v, w in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # DFS to get a pre-order traversal
    def dfs(v, visited, tour):
        visited.add(v)
        tour.append(v)
        for neighbor in adj_list[v]:
            if neighbor not in visited:
                dfs(neighbor, visited, tour)
                tour.append(v)  # Return to the node for TSP tour

    tour = []
    visited = set()
    dfs(0, visited, tour)

    # Remove duplicate visits while keeping the circuit complete
    visited = set()
    final_tape = []
    for city in tour:
        if city not in visited or city == 0:
            final_tape.append(city)
            visited.add(city)

    # Calculate the total travel cost of the tour
    travel_cost = sum(graph(final_tape[i], final_tape[i+1]) for i in range(len(final_tape)-1))

    return final_take, travel_cost

# Prepare graph for TSP calculation
graph = complete_graph(cities)

# Calculate the TSP tour and cost
tour, total_travel_cost = double_tree_tsp(nodes, mst, graph)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")