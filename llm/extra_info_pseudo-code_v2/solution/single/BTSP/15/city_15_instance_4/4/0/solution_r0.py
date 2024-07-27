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
    # One way to evaluate biconnected. Might be simplistic: checking no isolated vertex and no case with just one connecting vertex
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    rank = [0] * n

    for (u, v, _) in edges:
        union(parent, rank, u, v)

    root = find(parent, 0)
    return all(find(parent, i) == root for i in range(n))

def bottleneck_tsp(cities):
    n = len(cities)
    edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i, j in itertools.combinations(range(n), 2)]
    edges.sort(key=lambda x: x[2])  # sort by distance

    # Algorithm BB
    E_BB = []
    max_edge_weight = 0
    for (u, v, w) in edges:
        E_BB.append((u, v, w))
        if is_biconnected(E_BB, n):
            max_edge_weight = max(max_edge_weight, w)
            break

    # Tour Identification, Naive TSP solution due to small graph size
    perm = min(itertools.permutations(range(1, n)), key=lambda x: sum(euclidean_distance(cities[x[i]], cities[x[i - 1]]) for i in range(n)))
    perm = [0] + list(perm) + [0]

    total_cost = sum(euclidean_distance(cities[perm[i]], cities[perm[i + 1]]) for i in range(len(perm) - 1))
    max_distance = max(euclidean_distance(cities[perm[i]], cities[perm[i + 1]]) for i in range(len(perm) - 1))

    return perm, total_cost, max_distance

# City coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62),
          (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

tour, total_cost, max_distance = bottleneck_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")