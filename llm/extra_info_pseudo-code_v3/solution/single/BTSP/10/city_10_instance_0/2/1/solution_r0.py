import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def has_hamiltonian_path(edges, num_nodes):
    """ 
    A simplistic check for a Hamiltonian path which checks for paths using backtracking. 
    For large number of nodes, this needs a better method due to computational complexity reasons.
    """
    def backtrack(current_node, visited, path):
        if len(path) == num_nodes:
            path.append(path[0])  # To make it a cycle, return to the starting node
            return path
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(neighbor, visited, path + [neighbor])
                if result:
                    return result
                visited.remove(neighbor)
        return None

    # Create graph from edges
    graph = {i: set() for i in range(num_nodes)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Try to find a Hamiltonian path from any start node
    for start in range(num_nodes):
        visited = set([start])
        path = [start]
        result = backtrack(start, visited, path)
        if result:
            return result
    return None

def bottleneck_tsp(cities):
    num_cities = len(cities)
    edges = [
        (i, j, euclidean_to_int_distance(cities[i], cities[j]))
        for i in range(num_cities) for j in range(i + 1, num_cities)
    ]
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for max_edge_weight in set(edge[2] for edge in edges):
        filtered_edges = [(u, v) for u, v, w in edges if w <= max_edge_weight]
        path = has_hamptonian_path(filtered_edges, num_cities)
        if path:
            tour_cost = sum(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
            max_segment_length = max(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
            return {'Tour': path, 'Total travel cost': tour_cost, 'Maximum distance between consecutive cities': max_segment_length}

def euclidean_to_int_distance(p1, p2):
    return round(euclidean_distance(p1, p2) * 1000)

# Define the cities (Node 0 is depot)
cities = [
    (50, 42),  # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

result = bottleneck_tsp(cities)
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel cost'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive']