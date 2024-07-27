import math
import itertools

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Mapping cities to their Euclidean distances
edges = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Function to check if a graph is connected
def is_connected(subgraph, nodes):
    visited = set()
    
    def dfs(node):
        visited.add(node)
        for n in nodes:
            if (node, n) in subgraph or (n, node) in subgraph:
                if n not in visited:
                    dfs(n)
                    
    # Start DFS from the first node in list
    dfs(nodes[0])
    return visited == set(nodes)

# Bottle-neck Biconnected Subgraph (BB)
def find_bottleneck_biconnected_subgraph():
    nodes = list(cities.keys())
    subgraph = set()
    
    for edge, _ in sorted_edges:
        subgraph.add(edge)
        if is_connected(subgraph, nodes):
            # Check biconnectivity by removing each edge and seeing if the graph remains connected
            for e in subgraph:
                if not is_connected(subgraph - {e}, nodes):
                    break
            else:
                # It's biconnected as removing any edge keeps it connected
                return subgraph, max(edges[edge] for edge in subgraph)
    
    return None, None

# Find a Hamiltonian path that is a circle starting back at 0
def find_tour(subgraph):
    nodes = list(cities.keys())
    tour = [0]
    available_edges = {edge for edge in subgraph if 0 in edge}
    
    while len(tour) < len(nodes):
        for edge in available_edges:
            if tour[-1] in edge:
                next_node = edge[1] if edge[0] == tour[-1] else edge[0]
                if next_node not in tour:
                    tour.append(next_node)
                    available_edges = {e for e in subgraph if tour[-1] in e}
                    break
    
    tour.append(0)  # Complete the circuit back to the depot
    return tour

# Main execution to determine the tour
subgraph, bottleneck_cost = find_bottleneck_biconnected_subgraph()
tour = find_tour(subgraph)

# Calculate the metrics for the tour
max_distance = 0
total_cost = 0

for i in range(len(tour) - 1):
    dist = edges[(tour[i], tour[i+1])]
    total_cost += dist
    max_distance = max(max_distance, dist)

output = {
    "Tour": tour,
    "Total travel crash cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(output)