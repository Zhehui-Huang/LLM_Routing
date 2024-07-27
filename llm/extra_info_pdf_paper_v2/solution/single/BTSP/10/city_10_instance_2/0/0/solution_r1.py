import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Compute all distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Minimum Spanning Tree using Prim's Algorithm
import heapq

def minimum_spanning_tree(start, distances):
    connected = set([start])
    edges = [(cost, start, to) for to, cost in distances[start].items()]
    heapq.heapify(edges)
    mst = []
    while edges and len(connected) < len(cities):
        cost, frm, to = heapq.heappop(edges)
        if to not in connected:
            connected.add(to)
            mst.append((frm, to))
            for next_city, next_cost in distances[to].items():
                if next_city not in connected:
                    heapq.heappush(edges, (next_cost, to, next_city))
    return mstr

# Construct full list of distances
for i in cities:
    distances[i] = {j: distances[(min(i, j), max(i, j))] for j in cities if i != j}

mst = minimum_spanning_tree(0, distances)

# Trace a path through the MST using DFS to create a tour
def create_tour(start, graph):
    tour = []
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            tour.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return tour

# Convert MST to adjacency list form
graph = {i: [] for i in cities}
for frm, to in mst:
    graph[frm].append(to)
    graph[to].append(frm)

tour = create_tour(0, graph) + [0]  # tour back to the start

# Calculate total cost and max distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_leg_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_leg_distance)