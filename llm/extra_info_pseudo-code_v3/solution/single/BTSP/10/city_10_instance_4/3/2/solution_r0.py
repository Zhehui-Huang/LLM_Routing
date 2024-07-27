import networkx as nx
import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            d = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=d)
    return G

def get_sorted_edges(G):
    return sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

def has_hamiltonian_path(G, n):
    # A simple approach to check if there exists a Hamiltonian path
    # Not optimal and not always correct: using DFS to try all permutations
    def dfs(node, visited, path):
        if len(path) == n:
            all_visited = all(visited)
            return all_visited, path
        for neighbor in G.neighbors(node):
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                found, res_path = dfs(neighbor, visited, path)
                if found:
                    return True, res_path
                visited[neighbor] = False
                path.pop()
        return False, []

    for node in G.nodes():
        visited = [False] * n
        visited[node] = True
        path = [node]
        found, path = dfs(node, visited, path)
        if found:
            return True, path
    return False, []

def btsp(cities):
    G = generate_graph(cities)
    sorted_edges = get_sorted_edges(G)
    
    for weight in sorted(set([data['weight'] for _, _, data in sorted_edges])):
        bottleneck_graph = nx.Graph()
        bottleneck_graph.add_nodes_from(G.nodes())
        for u, v, data in sorted_edges:
            if data['weight'] <= weight:
                bottleneck_graph.add_edge(u, v, weight=data['weight'])

        if nx.is_connected(bottleneck_graph) and len(max(nx.connected_components(bottleneck_graph), key=len)) == len(cities):
            has_path, path = has_hamiltonian_path(bottleneck_graph, len(cities))
            if has_path:
                path.append(path[0])  # to make it a tour
                # Calculate total cost and maximal edge cost
                max_edge = 0
                total_cost = 0
                for i in range(len(path) - 1):
                    edge_weight = euclidean_distance(cities[path[i]], cities[path[i + 1]])
                    total_cost += edge_sha256
                    max_edge = max(max_edge, edge_weight)
                return {'Tour': path, 'Total travel cost': total_cost, 'Maximum distance between consecutive cities': max_edge}

    return None

# Cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62),
]

# Solve the problem
result = btsp(cities)
print(result)