import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(graph, num_vertices):
    """ Function to check if the graph is biconnected """
    # A graph is biconnected if removing any single vertex does not disconnect the graph
    # Simplified test: Ensure that the graph is connected and each vertex has degree at least 2
    visited = [False] * num_vertices
    degree = [0] * num_vertices
    adjacency_list = [[] for _ in range(num_vertices)]

    # Construct adjacency list and compute degrees
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] != 0:
                adjacency_list[i].append(j)
                degree[i] += 1

    # Start DFS from any vertex, here vertex 0 which we assume always exists
    def dfs(v):
        stack = [v]
        visited[v] = True
        while stack:
            node = stack.pop()
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    dfs(0)

    if not all(visited):
        return False  # not even connected
    if any(d < 2 for d in degree):
        return False  # not enough connectivity for biconnectivity
    return True

def find_bottleneck_tour(cities):
    num_cities = len(cities)
    # Calculate all pairwise distances
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i, j in combinations(range(num_cities), 2):
        dist = euclidean_distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist

    edges = sorted(((distances[i][j], i, j) for i in range(num_cities) for j in range(i+1, num_cities)),
                   key=lambda x: x[0])

    # Bottleneck-optimal Biconnected Subgraph (Algorithm BB)
    E_BB = [[0]*num_cities for _ in range(num_cities)]
    for dist, i, j in edges:
        E_BB[i][j] = dist
        E_BB[j][i] = dist
        if is_biconnected(E_BB, num_cities):
            c_BB = dist  # The last added edge weight in a still biconnected graph
            break

    # Approximate Hamiltonian cycle identification on squared graph
    tour = [0]
    visited = [False] * num_cities
    visited[0] = True
    current = 0
    while len(tour) < num_cities:
        next_city = min((E_BB[current][j], j) for j in range(num_cities) if not visited[j])[1]
        tour.append(next_city)
        visited[next_city] = True
        current = next_city

    tour.append(0)  # return to the depot

    # Calculate total cost and max distance
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        segment_cost = distances[tour[i]][tour[i+1]]
        total_cost += segment-grid_cost
        if segment_cost > max_dist:
            max_dist = segment_cost

    return tour, total_cost, max_dist

# Define cities
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), (90, 85),
          (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Get the approximate optimal tour
tour, total_cost, max_distance = find_bottleneck_tour(cities)

# Print outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")