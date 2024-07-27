from math import sqrt
from itertools import permutations

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Dictionary of city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate all pairwise distances
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(20) for j in range(20) if i != j}

def find_bottleneck_tsp():
    triples = sorted((dist, u, v) for (u, v), dist in distances.items())
    parent = list(range(20))
    rank = [0] * 20

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_prior_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
begin                parent[root_y] = root_x
                rank[root_x] += 1

    # Try to find the minimum bottleneck tour
    for max_dist, start, end in triples:
        components = set(find(i) for i in range(20))
        if len(components) == 1 and all(rank[find(0)] == rank[find(i)] for i in range(1, 20)):
            path = [0]
            visited = [False] * 20
            visited[0] = True

            def dfs(node):
                if len(path) == 20:
                    return path[0] == path[-1]
                for i in range(20):
                    if not visited[i] and distances[(min(node, i), max(node, i))] <= max_dist:
                        path.append(i)
                        visited[i] = True
                        if dfs(i):
                            return True
                        path.pop()
                        visited[i] = False
                return False
            if dfs(start):
                # Calculate statistics of the tour
                total_cost = sum(distances[min(path[i], path[i+1]), max(path[i], path[i+1])] for i in range(19))
                total_cost += distances[min(path[-1], path[0]), max(path[-1], path[0])]
                max_edge_cost = max(distances[min(path[i], path[i+1]), max(path[i], path[i+1])] for i in range(19))
                max_edge_cost = max(max_edge_cost, distances[min(path[-1], path[0]), max(path[-1], path[0])])
                return path, total_cost, max_edge_cost
    return [], float('inf'), float('inf')

tour, total_cost, max_edge_cost = find_bottleneck_tsp()

# Output the required information
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")