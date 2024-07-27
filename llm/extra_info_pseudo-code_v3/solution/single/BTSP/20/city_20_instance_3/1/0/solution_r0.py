import math
import networkx as nx

# Coordinates of the cities
cities = [
    (30, 56),  # Depot city 0
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Number of cities
num_cities = len(cities)

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a list of all edges with distances
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((i, j, dist))

# Sort edges by distance
edges.sort(key=lambda e: e[2])

# Construct the bottleneck graph for each unique distance and check for Hamiltonian path
def check_hamiltonian_path(G, n):
    """ Use heuristic to check for Hamiltonian path; for simplicity, analyzer degree and connectivity """
    if nx.is_connected(G):
        # A very naive check: if connected and n-1 edges
        if G.number_of_edges() >= n - 1:
            try:
                cycle = nx.approximation.traveling_salesman_problem(G, cycle=True)
                if len(cycle) == n + 1 and cycle[0] == cycle[-1]:
                    return cycle[:-1]  # Return valid cycle minus the repeated last node
            except nx.NetworkXError:
                pass
    return None

# Iterative check over sorted edges until Hamiltonian path found
def find_btsp_path(edges, n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    for (u, v, d) in edges:
        G.add_edge(u, v, weight=d)
        cycle = check_hamiltonian_path(G, n)
        if cycle is not None:
            return cycle, d
    return None, None

# Get the Hamiltonian cycle
cycle, max_edge_weight = find_btsp_path(edges, num_cities)

# If a cycle is found, compute details
if cycle:
    cycle.append(cycle[0])  # to complete the tour
    # Calculate total travel cost
    total_cost = sum(euclidean_distance(cities[cycle[i]], cities[cycle[i + 1]]) for i in range(len(cycle) - 1))
    
    # Print the results as required
    print(f"Tour: {cycle}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_edge_weight:.2f}")
else:
    print("No suitable Hamiltonian circuit found.")