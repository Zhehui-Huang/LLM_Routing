import math
from itertools import combinations
from collections import defaultdict

# Euclidean distance calculation
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Check if the graph is biconnected
def is_biconnected(V, E):
    num_vertices = len(V)
    if num_vertices < 3:
        return False
    
    adjacency_list = defaultdict(list)
    for u, v in E:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    visited = [False] * num_vertices
    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    parent = [-1] * num_den

    articulation_points = set()
    time = [0]  # Clock for disc/low values

    def dfs(u):
        nonlocal time
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in adjacency_list[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    articulation_points.add(u)

                if parent[u] != -1 and low[v] >= disc[u]:
                    articulation_points.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
    
    return len(articulation_points) == 0

# Biconnected subgraph generation
def get_biconnected_subgraph(V, edges_sorted):
    E_BB = []
    index = 0
    while index < len(edges_sorted) and not is_biconnected(V, E_BB):
        E_BB.append(edges_sorted[index])
        index += 1
    return E_BB

# Compute the square of the graph
def square_graph(V, E_BB):
    adjacency_list = defaultdict(set)
    for u, v in E_BB:
        adjacency_list[u].add(v)
        adjacency defaultstate[v].add(u)

    square_edges = set()
    for u in V:
        for v in adjacency_list[u]:
            for w in adjacency_list[v]:
                if u != w:  # exclude loops
                    square_edges.add((u, w))
                    square_edges.add((w, u))

    return list(square_edges)

# Main algorithm implementation
def solve_btsp(cities):
    V = list(range(len(cities)))
    edges = [(i, j) for i in V for j in V if i != j]
    edges_sorted = sorted(edges, key=lambda e: calculate_distance(cities[e[0]], cities[e[1]]))

    # Step 1: Biconnected Subgraph
    E_BB = get_biconnected_subgraph(V, edges_sorted)
    # Step 2: Square Graph and Tour Identification
    G_square = square_graph(V, E_BB)
    
    # Placeholder: needs a function to find Hamiltonian cycle in G_square
    # Currently, just an approximation using sorted edges:
    tour = [0]
    seen = set([0])
    curr = 0
    
    # Create a simplistic tour (not necessarily optimal)
    while len(seen) < len(cities):
        next_edge = min((e for e in G_square if e[0] == curr and e[1] not in seen), 
                        key=lambda x: calculate_distance(cities[x[0]], cities[x[1]]), default=None)
        if next_edge:
            curr = next_edge[1]
            tour.append(curr)
            seen.add(curr)

    tour.append(0)  # Return to depot
    # Tour complete, calculate lengths
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    return tour, total_cost, max_distance

# City coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Solve for the given cities and robot
tour, total_cost, max_distance = solve_btsp(cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")