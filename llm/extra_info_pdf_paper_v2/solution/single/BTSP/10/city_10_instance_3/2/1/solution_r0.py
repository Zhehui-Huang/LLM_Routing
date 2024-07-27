import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City location data as a dictionary {city_index: (x_coord, y_coord)}
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Compute edge cost (distance matrix)
edges = {}
for i, j in combinations(cities.keys(), 2):
    distance = euclidean_distance(cities[i], cities[j])
    edges[(i, j)] = distance
    edges[(j, i)] = distance

def minimum_spanning_tree(vertices, edges):
    # Using Kruskal's algorithm for finding MST
    from heapq import heappush, heappop
    connected = []
    for v in vertices:
        connected.append({v})
    
    def find_set(sets, v):
        for subset in sets:
            if v in subset:
                return subset
    
    mst = []
    edge_list = [(edges[(u, v)], u, v) for u, v in combinations(vertices, 2)]
    edge_list.sort()
    
    while len(mst) < len(vertices) - 1:
        weight, u, v = edge_list.pop(0)
        set_u = find_set(connected, u)
        set_v = find_set(connected, v)
        if set_u != set_v:
            mst.append((u, v))
            new_set = set_u.union(set_v)
            connected.remove(set_u)
            connected.remove(set_v)
            connected.append(new_set)

    return mst

def find_bottleneck_tour(vertices, edges):
    # Find MST
    mst_edges = minimum_spanning_tree(vertices, edges)
    
    # Create a multigraph by doubling edges of the MST
    multigraph_edges = mst_edges + mst_edges
    
    # Find an Eulerian circuit in the multigraph (Hierholzer’s algorithm)
    from collections import deque, defaultdict

    graph = defaultdict(list)
    for u, v in multigraph_edges:
        graph[u].append(v)
        graph[v].append(u)

    # Start from the depot (vertex 0)
    start_vertex = 0
    stack = [start_vertex]
    path = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
            graph[u].remove(v)
        else:
            path.append(stack.pop())
    
    # Making it a tour: start and end at the depot
    path = path[::-1]  # Reverse path
    
    # Short circuiting the Eulerian tour to make a valid TSP tour by skipping repeated vertices
    seen = set()
    tour = []
    for city in path:
        if city not in seen:
            tour.append(city)
            seen.add(city)
    tour.append(tour[0])  # End tour at the starting point
    
    # Calculate the costs
    total_cost = sum(edges[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    max_distance = max(edges[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

vertices = list(cities.keys())
tour, total_cost, max_distance = find_bottleneck_tour(vertices, edges)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))