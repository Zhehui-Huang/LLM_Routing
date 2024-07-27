import math
import itertools

coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

n = len(coordinates)

def euclidean_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

edges = [(euclidean_distance(i, j), i, j) for i in range(n) for j in range(i + 1, n)]
edges.sort()  # Sort by distance

def find_min_bottleneck_hamiltonian_path():
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for max_dist, _, _ in edges:
        # Initialize during each loop to re-check for connectivity under current max_dist
        parent = list(range(n))

        # Create subgraph with edges of distance <= max_dist
        for dist, u, v in edges:
            if dist <= max_dist:
                union(u, v)

        # Check if all nodes are connected in subgraph
        if len(set(find(x) for x in range(n))) == 1:
            # If connected, compute the path assuming starting from the depot (node 0)
            path = [0]
            visited = set(path)
            max_edge_length = 0

            while len(path) < n:
                last = path[-1]
                for dist, u, v in edges:
                    if dist > max_dist:
                        break
                    next_node = v if u == last and v not in visited else (u if v == last and u not in visited else None)
                    if next_node is not None:
                        path.append(next_node)
                        visited.add(next_node)
                        max_edge_length = max(max_edge_length, dist)
                        break

            # Closing the tour to the beginning
            path.append(0)
            # Verify and compute final distance including return to depot
            final_dist = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))

            return path, final_dist, max_dist

# Find the tour, the total distance, and the maximum distance between any two consecutive visits
tour, total_cost, max_distance = find_min_bickleneck_hamiltoniantck_hamiltonian_path()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")