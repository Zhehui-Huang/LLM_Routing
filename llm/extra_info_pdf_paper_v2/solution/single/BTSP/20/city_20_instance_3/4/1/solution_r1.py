import math
from scipy.spatial import distance_matrix
from heapq import heappop, heappush
from collections import defaultdict, deque

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def minimum_spanning_tree(cities):
    """ Uses Prim's algorithm to find the Minimum Spanning Tree """
    n = len(cities)
    adj_list = {i: [] for i in range(n)}
    min_edge = [(float('inf'), -1, i) for i in range(n)]
    min_edge[0] = (0, -1, 0)
    visited = [False] * n
    mst_edges = []
    edges_in_mst = []
    
    # Priority queue to select the edge with the minimum weight
    q = []
    for edge in min_edge:
        heappush(q, edge)
    
    while q:
        cost, frm, to = heappop(q)
        
        if visited[to]:
            continue
        
        visited[to] = True
        for i in range(n):
            if not visited[i] and i != to:
                weight = euclidean_distance(cities[to], cities[i])
                if weight < min_edge[i][0]:
                    min_edge[i] = (weight, to, i)
                    heappush(q, (weight, to, i))
        
        if frm != -1:
            adj_list[frm].append(to)
            adj_list[to].append(frm)
            edges_in_mst.append((frm, to, cost))
    
    return edges_in_mst, adj_list

def preorder_walk(adj_list, start):
    """ Generate a preorder walk of the minimum spanning tree """
    tour = []
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            tour.append(node)
            for neighbor in reversed(adj_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return tour

def create_full_tour(preorder_tour):
    """ Make sure the tour is a full cycle returning to the start point """
    tour = list(preorder_tour) 
    tour.append(tour[0]) # return to start
    return tour

def calculate_metrics(tour, cities):
    max_dist = 0
    total_cost = 0
    previous_city = tour[0]
    
    for city in tour[1:]:
        dist = euclidean_distance(cities[previous_city], cities[city])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
        previous_city = city
    
    return total_cost, max_dist

# Coordinates of cities
coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Processing
mst_edges, adj_list = minimum_spanning_tree(coords)
preorder_tour = preorder_walk(adj_list, 0)
full_tour = create_full_tour(preorder_tour)
total_cost, max_distance = calculate_metrics(full_tour, coords)

# Output results
print("Tour:", full_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))