import math
from heapq import heappop, heappush

# Coordinates of cities
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities
n = len(coordinates)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    dx = coordinates[city1][0] - coordinates[city2][0]
    dy = coordinates[city1][1] - coordinates[city2][1]
    return math.sqrt(dx * dx + dy * dy)

# Construct complete graph with edges weighted by the distance
def construct_complete_graph():
    graph = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(i, j)
            graph[i][j] = dist
            graph[j][i] = dist
    return graph

# Prim's algorithm to find MST
def minimal_spanning_tree(graph, start_vertex):
    mst = {start_vertex}
    edges = [(cost, start_vertex, to) for to, cost in graph[start_start_vertex].items()]
    heapify(edges)
    mst_edges = []
    
    while edges:
        cost, frm, to = heappop(edges)
        if to not in mst:
            mst.add(to)
            mst_edges.append((frm, to, cost))
            for next_to, next_cost in graph[to].items():
                if next_to not in mst:
                    heappush(edges, (next_cost, to, next_to))
    return mst_edges

# Function to find a tour starting and ending at the starting vertex
def find_tour(edges, start_vertex):
    # Create adjacency list
    adj_list = {i: [] for i in range(n)}
    for u, v, _ in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Depth-first search to find a tour
    tour = []
    visit(tour, adj_list, start_vertex)
    tour.append(start_vertex)  # End at starting vertex (make a cycle)
    return tour

# Recursive DFS to record tour path
def visit(tour, adj_list, node):
    while adj_list[node]:
        next_node = adj_list[node].pop()
        visit(tour, adj_list, next_node)
    tour.append(node)

# Main computation
graph = construct_complete_graph()
mst_edges = minimal_spanning_tree(graph, 0)
tour = find_tour(mst_edges, 0)

# Calculate total travel cost and max distance
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distance(tour[i-1], tour[i])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output the result
print('Tour:', tour)
print('Total travel cost:', total_cost)
print('Maximum distance between consecutive cities:', max_distance)