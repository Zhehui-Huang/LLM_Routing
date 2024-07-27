import itertools
import math

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Function to compute Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Function to check if a set of edges is biconnected
def is_biconnected(graph, V):
    """
    Simple connectivity check for biconnectivity in undirected graph
    """
    start_node = next(iter(graph))
    stack = [start_node]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return len(visited) == V

# Algorithm BB to find bottleneck-optimal biconnected subgraph
def algorithm_bb(cities):
    num_cities = len(cities)
    edges = [(i, j, distance(i, j)) for i in range(num_cities) for j in range(i+1, num_cities)]
    edges.sort(key=lambda x: x[2])  # Sort by distance

    graph = {i: [] for i in range(num_cities)}
    E_BB = []
    for (i, j, d) in edges:
        graph[i].append(j)
        graph[j].append(i)
        E_BB.append((i, j, d))
        if is_biconnected(graph, num_cities):
            break
        else:
            graph[i].remove(j)
            graph[j].remove(i)
            E_BB.remove((i, j, d))

    return E_BB

# Identify the tour using returned biconnected edges
def find_tour(E_BB):
    graph = {i: [] for i in range(len(cities))}
    for i, j, _ in E_BB:
        graph[i].append(j)
        graph[j].append(i)

    # Start from depot 0
    current_city = 0
    tour = [current_city]
    visited = {current_city}
    while len(tour) < len(cities):
        next_city = min((city for city in graph[current_city] if city not in visited), key=lambda x: distance(current_city, x))
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city

    # Return to depot
    tour.append(0)
    return tour

# Retrieve E_BB which contains biconnected edges
E_BB = algorithm_bb(cities)

# Compute the tour from the biconnected graph
tour = find_tour(E_BB)

# Calculate the travel costs and the maximum distance between consecutive cities
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")