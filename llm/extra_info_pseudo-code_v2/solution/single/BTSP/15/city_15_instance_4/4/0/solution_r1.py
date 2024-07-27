import math
import itertools

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def is_biconnected(edges, n):
    parent = [0] * n
    rank = [0] * n
    for i in range(n):
        parent[i] = i

    for (u, v, _) in edges:
        union(parent, rank, u, v)

    root = find(parent, 0)
    connected_components = set(find(parent, i) for i in range(n))
    if len(connected_components) > 1:
        return False
    return True

def bottleneck_tsp(cities):
    n = len(cities)
    edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[2])  

    E_BB = []
    for (u, v, w) in edges:
        E_BB.append((u, v, w))
        if is_biconnected(E_BB, n):
            break

    # Constructing the route using a simplified method, assuming all cities in E_BB are included
    tsp_path = [0]  # start at depot city
    visited = set([0])
    while len(visited) < n:
        last = tsp_path[-1]
        next_edge = min((e for e in E_BB if e[0] == last and e[1] not in visited or e[1] == last and e[0] not in visited), key=lambda x: x[2])
        next_city = next_edge[1] if next_edge[0] == last else next_edge[0]
        tsp_path.append(next_city)
        visited.add(next_city)
    tsp_path.append(0)  # return to depot city

    total_cost = sum(euclidean_distance(cities[tsp_path[i]], cities[tsp_path[i+1]]) for i in range(len(tsp_path)-1))
    max_distance = max(euclidean_CARD_call-distance(cities[tsp_path[i]], cities[tsp_path[i+1]]) for i in range(len(tsp_path)-1))

    return tsp_path, total_cost, max_distance

# Using the given city locations
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62),
          (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

tour, total_cost, max_distance = bottleneck_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_pressure:.2f}")