import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = [
    (16, 90),  # Depot city
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def create_sorted_edges(cities):
    num_cities = len(cities)
    edges = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                edges.append((dist, i, j))
    edges.sort()
    return edges

def can_form_tour(graph, node_count):
    """ This function checks if all the nodes in the graph are connected as a single component and all nodes can be visited exactly once. """
    visited = [False] * node_count

    # Finding first node with any connection to start DFS
    start = next(i for i, adj in enumerate(graph) if adj)

    def dfs(v):
        stack = [v]
        count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                count += 1
                stack.extend(graph[node])
        return count

    # Check all nodes are reachable and entire connected component is visited exactly once
    return dfs(start) == node_count

def find_btsp_tour(cities):
    edges = create_sorted_edges(cities)
    num_cities = len(cities)

    for max_dist, i, j in edges:
        # Create graph with distances less than or equal to current max_dist
        graph = [[] for _ in range(num_cities)]
        for dist, u, v in edges:
            if dist <= max_dist:
                graph[u].append(v)
                graph[v].append(u)

        # Check if this graph has a Hamiltonian Cycle
        if can_form_tour(graph, num_cities):
            # To form Hamiltonian cycle, start and end at the depot (city 0)
            tour = [0]
            visited = [False] * num_cities
            visited[0] = True
            current = 0

            for _ in range(1, num_cities):
                next_city = min((u for u in graph[current] if not visited[u]), key=lambda x: euclidean_distance(cities[current], cities[x]))
                tour.append(next_city)
                visited[next_city] = True
                current = next_city

            tour.append(0)  # return to depot
            total_cost = sum(euclidean------------<
            print("Determining costs and maximum distance...")
            max_consecutive_dist = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            return tour, total_cost, max_consecutive_dist

    return None

result = find_btsp_tour(cities)
if result:
    tour, total_cost, max_consecutive_dist = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_consecutive_dist)
else:
    print("No feasible tour found.")