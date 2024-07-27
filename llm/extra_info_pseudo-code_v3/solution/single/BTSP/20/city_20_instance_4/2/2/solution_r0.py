import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (26, 60),  # Depot
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Calculate all pairwise distances
edge_weights = []
n = len(cities)
for i in range(n):
    for j in range(i+1, n):
        dist = calculate_distance(cities[i], cities[j])
        edge_weights.append((dist, i, j))

# Sort edges by weight
edge_weights.sort()

# Approximate BTSP
def has_valid_bottleneck_cycle(c_i):
    # Use a simple heuristic: Kruskal's algorithm for MST
    edges_used = []
    parent = list(range(n))
    rank = [0] * n

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    for dist, u, v in edge_weights:
        if dist > c_i:
            break
        if find(u) != find(v):
            union(u, v)
            edges_used.append((dist, u, v))
            if len(edges_used) == n - 1:
                # Check if all vertices are connected
                if len(set(find(x) for x in range(n))) == 1:
                    # Construct the path through an Euler circuit mechanism if feasible
                    if all(deg.count(1) == 2 for deg in itertools.groupby(sorted([u, v for _, u, v in edges_used]))):
                        # We assume the cycle can be traversed here as a path check (for simplicity)
                        return edges_used
    return None

best_path = None
for dist, _, _ in edge_weights:
    potential_path = has_valid_bottleneck_cycle(dist)
    if potential_path:
        best_path = potential_path
        max_dist = dist
        break

if best_path:
    tour = [0]
    # Constructing path from edges (heuristic approach)
    current_city = 0
    visited = set([0])
    while len(visited) < n:
        for _, u, v in best_path:
            if u == current_city and v not in visited:
                tour.append(v)
                visited.add(v)
                current_city = v
                break
            elif v == current_city and u not in visited:
                tour.append(u)
                visited.add(u)
                current_city = u
                break
    # Connect back to the depot.
    tour.append(0)

    total_cost = sum(calculate_distance(cities[tour[idx]], cities[tour[idx+1]]) for idx in range(len(tour)-1))

    # Output
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("Failed to find a valid tour.")