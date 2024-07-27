from heapq import heappop, heappush
from collections import defaultdict

def is_biconnected(graph, n):
    """Returns True if the graph is biconnected using a single DFS."""
    def dfs(u, parent):
        nonlocal time
        discovery[u] = low[u] = time
        time += 1
        children = 0

        for v in graph[u]:
            if discovery[v] == -1:  # v is not visited
                parent[v] = u
                children += 1
                dfs(v, parent)
                low[u] = min(low[u], low[v])

                # If u is the root with at least two children, it's an articulation point
                if parent[u] == -1 and children > 1:
                    is_artic.append(True)
                
                # If u is not root and low value of one of its child is more than discovery value of u.
                if parent[u] != -1 and low[v] >= discovery[u]:
                    is_artic.append(True)

            elif v != parent[u]:  # Update low value of u for parent function calls.
                low[u] = min(low[u], discovery[v])

    is_artic = []
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    time = 0

    # Call the recursive DFS to find the articulation points
    dfs(0, parent)

    # If no articulation point found, the graph is biconnected
    return not is_artic

def find_bottleneck_optimal_biconnected_subgraph(city_distances, n):
    # Sort edges by weight
    sorted_edges = sorted((distance, min(i, j), max(i, j)) for ((i, j), distance) in city_distances.items())
    bb_graph = defaultdict(set)  # Using a set for each node to easily manage connections
    bb_edges = []

    # Kruskal's-like process to build a bottle-neck optimal subgraph
    for cost, i, j in sorted_edges:
        bb_graph[i].add(j)
        bb_graph[j].add(i)
        bb_edges.append((cost, i, j))

        # Check if currently biconnected
        if is_biconnected(bb_graph, n):
            return bb_edges, cost
        # If not, continue adding edges

def squared_graph_biconnected(edges, n):
    # Create graph square for bottleneck optimal graph
    graph = defaultdict(set)
    for cost, i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    # Squaring the graph: nodes are connected in the subgraph if they are at most 2 edges away
    square_graph = defaultdict(set)
    for v in graph:
        for u in graph[v]:
            for w in graph[u]:
                if w != v:
                    square_graph[v].add(w)
    return square_graph

def find_approximate_tour(graph_square, start, n):
    # Using a simple greedy nearest neighbour algorithm to find a tour in squared graph
    current = start
    visited = set([start])
    tour = [start]

    while len(visited) < n:
        next_city = min((city for city in graph_square[current] if city not in visited), key=lambda x: city_distances[(current, x)], default=None)
        if next_city is None:
            break
        tour.append(next_city)
        visited.add(next_city)
        current = next_city

    # Connect back to start to complete the cycle if possible
    if start in graph_square[current]:
        tour.append(start)
    
    return tour

def calculate_tour_costs(tour, city_distances):
    total_cost = sum(city_distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    max_cost = max(city_distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    return total_cost, max_cost

# Finding the biconnected subgraph
n = len(cities)
edges_biconnected, max_cost_biconnected = find_bottleneck_optimal_biconnected_subgraph(city_distances, n)

# Construct the squared graph of the biconnected subgraph
squared_graph = squared_graph_biconnected(edges_biconnected, n)

# Find an approximate Hamiltonian cycle in the squared graph
tour = find_approximate_tour(squared_graph, 0, n)

# Calculate costs for the obtained tour
total_travel_cost, max_distance_consecutive_cities = calculate_tour_costs(tour, city_distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_st_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_consecutive_cities}")