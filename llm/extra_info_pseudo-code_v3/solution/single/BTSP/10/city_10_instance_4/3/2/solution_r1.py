import networkx as nx
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def generate_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            d = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=d)
    return G

def get_sorted_edges(G):
    return sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

def find_hamiltonian_path(n, edges):
    for perm in permutations(range(n)):
        if perm[0] == 0:  # start from depot city 0
            valid_path = True
            for i in range(1, len(perm)):
                if (perm[i-1], perm[i]) not in edges and (perm[i], perm[i-1]) not in edges:
                    valid_path = False
                    break
            if valid_path:
                return True, perm
    return False, []

def btsp(cities):
    G = generate_graph(cities)
    sorted_edges = get_sorted_edges(G)
    
    for threshold in sorted(set(data['weight'] for _, _, data in sorted_edges)):
        valid_edges = {(u, v) for u, v, d in sorted_edges if d['weight'] <= threshold}
        has_path, path = find_hamiltonian_path(len(cities), valid_edges)
        if has_path:
            path += (path[0],)  # Make it a tour by returning to the start node
            # Calculate maximum edge cost and total cost
            max_edge = 0
            total_cost = 0
            for i in range(len(path) - 1):
                distance = euclidean_distance(cities[path[i]], cities[path[i + 1]])
                total_cost += distance
                max_edge = max(max_edge, distance)
            return {'Tour': path, 'Total travel cost': round(total_cost, 2), 'Maximum distance between consecutive cities': round(max_edge, 2)}
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