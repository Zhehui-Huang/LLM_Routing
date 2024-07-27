import math
import heapq
from collections import defaultdict

# Define the cities with their coordinates
city_positions = [
    (53, 68),  # City 0: Depot
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find(parent, i):
    if parent[i] == i:
        return i
    else:
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

def kruskal(num_vertices, edges):
    result = []  # This will store the resultant MST
    i = 0  # An index variable for sorted edges
    e = 0  # An index variable for result[]
  
    # Step 1: Sort all the edges in non-decreasing order of their weight.
    edges = sorted(edges, key=lambda item: item[0])
  
    parent = []
    rank = []
  
    # Create V subsets with single elements
    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)
  
    while e < num_vertices - 1:
        w, u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
  
        if x != y:
            e = e + 1
            result.append((w, u, v))
            union(parent, rank, x, y)
  
    return result

def form_tour(edges, num_vertices):
    # Create adjacency list of the MST
    graph = defaultdict(list)
    for w, u, v in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Start from the depot (node 0), perform DFS to get a tour
    visit = set()
    stack = [0]
    tour = []

    while stack:
        node = stack.pop()
        if node in visit:
            continue
        visit.add(node)
        tour.append(node)

        for neighbor, weight in reversed(graph[node]):
            if neighbor not in visit:
                stack.append(neighbor)

    return tour

# Compute all pairwise distances
edges = []
num_vertices = len(city_positions)
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        dist = euclidean_distance(city_positions[i], city_positions[j])
        edges.append((dist, i, j))

# Generate MST focusing to minimize the max edge weight
mst_edges = kruskal(num_vertices, edges)

# Form the tour
tour = form_tour(mst_edges, num_vertices)
tour.append(tour[0])  # Make it a cycle by returning to the start

# Calculate the total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))