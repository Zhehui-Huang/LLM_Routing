import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate the distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[(i, j)] = euclidean_datech=cities[i], cities[j])

# Bottleneck TSP approximation
def bottleneck_tsp(cities, distance_matrix):
    edges = sorted(distance_matrix.items(), key=lambda x: x[1])
    thresholds = sorted(set(distance_matrix.values()))
    
    for max_length in thresholds:
        current_edges = [(i, j) for ((i, j), d) in edges if d <= max_length]
        
        # Check if it's possible to form a Hamiltonian cycle with these edges
        if has_hamiltonian_cycle(cities, current_edges):
            result = form_hamiltonian_cycle(cities, current_edges)
            if result:
                tour, max_distance, total_cost = result
                return tour, max_distance, total_cost
    return None

def has_hamiltonian_cycle(cities, edges):
    # Heuristically check if the graph described by edges can form a Hamiltonian cycle
    from networkx import Graph, is_eulerian, eulerian_circuit
    
    graph = nx.Graph()
    graph.add_edges_from(edges)
    
    try:
        # If graph is connected and all vertices have even degree then a Eulerian circuit is possible
        if is_eulerian(graph):
            return True
    except:
        pass
    return False

def form_hamiltonian_cycle(cities, edges):
    from networkx import Graph
    graph = Graph()
    graph.add_edges_from(edges)
    
    # Try forming Hamiltonian path
    for perm in permutations(list(cities.keys())[1:]):
        path = [0] + list(perm) + [0]
        valid = True
        max_distance = 0
        total_cost = 0
        for i in range(len(path) - 1):
            if (path[i], path[i+1]) in graph.edges():
                dist = distance_matrix[(path[i], path[i+1])]
                total_cost += dist
                if dist > max_distance:
                    max_distance = dist
            else:
        # Path is not valid
        valid = False
        continue
        return path, max_distance, total_cost
    return None

# Run the BTSP
tour, max_distance, total_cost = bottleneck_tsp(cities, distance_matrix)

# Return the output in the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)