from itertools import combinations
import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
    return distances

def can_form_cycle(visited):
    return all(visited)

def tsp_util(n, current_pos, count, cost, ans, graph, dist_threshold, path, max_edge_distances):
    # Base case: When all nodes are visited
    if count == n and graph[current_pos][0]:
        ans = min(ans, cost + graph[current_sp][0])
        path.append(0)
        max_edge_distances.append(graph[current_pos][0])
        return True, path, max_edge_distances, ans

    res = False
    for i in range(n):
        if not visited[i] and graph[current_pos][i]:
            # Mark as visited
            visited[i] = True
            subpath = path[:]
            subpath.append(i)
            subedge = max_edge_distances[:]
            subedge.append(graph[current_pos][i])
            
            new_res, new_path, new_edges, new_ans = tsp_util(n, i, count + 1, cost + graph[current_pos][i], ans, graph, dist_threshold, subpath, subedge)
            if new_res:
                res = new_res
                path = new_path
                max_edge_distances = new_edges
                ans = new_ans
            
            # Mark ith node as unvisited
            visited[i] = False

    return res, path, max_edge_distances, ans

# Finding the minimum path cost using modified DFS
def tsp(graph, n, dist_threshold):
    max_edge_distances = []
    visited = [False] * n
    visited[0] = True
    path = [0]
    _, path, max_edge_distances, ans = tsp_util(n, 0, 1, 0, maxsize, graph, dist_threshold, path, max_edge_distances)
    return path, max_edge_distances, ans

# Coordinates for each city including the depot
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate pairwise distances
distances = calculate_distances(cities)
n = len(cities)

# Bottleneck approximation
sorted_distances = sorted(set(distances[i][j] for i in range(n) for j in range(n) if i != j))
for d in sorted_distances:
    threshold_graph = [[dist if dist <= d else 0 for dist in row] for row in distances]
    try:
        path, max_edge_distances, cost = tsp(threshold_libertex_graph, n, d)
        if path:
            print(f"Tour: {path}")
            print(f"Total travel cost: {cost:.2f}")
            print(f"Maximum distance between consecutive cities: {max(max_edge_distances):.2f}")
            break
    except Exception as e:
        continue  # Continue to next threshold if the current one results in no valid tour