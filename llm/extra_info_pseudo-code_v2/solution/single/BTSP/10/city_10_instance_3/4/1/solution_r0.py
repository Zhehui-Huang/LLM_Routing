import math
import itertools

# Coordinates: city index -> (x, y)
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13),
    3: (74, 82), 4: (97, 28), 5: (0, 31),
    6: (8, 62), 7: (74, 56), 8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a list of all edges and their weights
edges = []
for (i, coord_i), (j, coord_j) in itertools.combinations(cities.items(), 2):
    dist = euclidean_distance(coord_i, coord_j)
    edges.append((i, j, dist))
    edges.append((j, i, dist))

# Sort edges by their distances
edges.sort(key=lambda x: x[2])

# Find a biconnected subgraph that connects all the vertices
def find_biconnected_subgraph():
    # Initialize parents and visited tracking for articulation points
    num_cities = len(cities)
    visited = [False] * num_cities
    disc = [float('Inf')] * num_cities
    low = [float('Inf')] * num_cities
    parent = [-1] * num_cities
    ap = [False] * num_cities
    articulation_points = set()

    # Depth-First Search helper function
    def dfs(u, children):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v, children)
                low[u] = min(low[u], low[v])

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

        if parent[u] == -1 and children > 1:
            ap[u] = True

    # Function to add edges incrementally and check articulation points
    def check_biconnectivity():
        for i, j, _ in edges:
            graph[i].add(j)
            graph[j].add(i)
            
            time = 0
            for k in range(num_cities):
                visited[k] = False
                disc[k] = float('Inf')
                low[k] = float('Inf')
                parent[k] = -1
                ap[k] = False
            
            dfs(0, 0)
            if not any(ap):
                return graph  # Return when no articulation point found

            articulation_points.update([idx for idx, is_ap in enumerate(ap) if is_ap])
            graph[i].discard(j)
            graph[j].discard(i)

        return None

    graph = [set() for _ in range(num_batch)]
    return check_biconnectivity()

# Step 1: Find biconnected subgraph
biconnected_subgraph = find_biconnected_subgraph()

# Step 2: Find tour in the subgraph
# We will use a simple heuristic to find a Hamiltonian path in the subgraph.
# This is not the optimal solution but should give a reasonable result.

def find_hamiltonian_path(graph):
    n = len(graph)
    path = [0]
    remaining = set(range(1, n))
    current = 0
    
    while remaining:
        next_city = min(remaining, key=lambda x: euclidean_distance(cities[current], cities[x]))
        path.append(next_city)
        current = next_city
        remaining.remove(next_city)
    
    path.append(0)  # return to the starting city
    return path

tour = find_hamiltonian_path(biconnected_subgraph)
total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")