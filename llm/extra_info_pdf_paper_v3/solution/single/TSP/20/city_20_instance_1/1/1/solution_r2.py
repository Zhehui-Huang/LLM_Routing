import math
import networkx as nx

# Define cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Christofides Algorithm Implementation
def christofides(G):
    # Minimum Spanning Tree (MST)
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # Find vertices with odd degree
    odd_vertices = [v for v, d in T.degree() if d % 2 != 0]
    
    # Minimum Cost Perfect Matching (MCPM)
    matching_graph = nx.Graph()
    matching_graph.add_nodes_from(odd_vertices)
    for pair in combinations(odd_vertices, 2):
        matching_graph.add_edge(pair[0], pair[1], weight=distance(pair[0], pair[1]))
    min_matching = nx.algorithms.matching.min_weight_matching(matching_graph, maxcardinality=True, weight='weight')
    
    T.add_edges_from(min_matching)
    
    # Create an Eulerian tour
    euler_circuit = list(nx.eulerian_circuit(T, source=0))
    
    path = [0]  # start from the depot city
    visited = set()
    visited.add(0)
    for u, v in euler_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(0)  # return to the starting city
    
    return path

# Execute the algorithm
tour = christofides(G)

# Calculate the cost of the returned tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Get the total cost of the tour
total_cost = calculate_tour_cost(tour)

# Present the results
output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_cost:.2f}"
output_t:\n{output_tour}\n{output_cost}")