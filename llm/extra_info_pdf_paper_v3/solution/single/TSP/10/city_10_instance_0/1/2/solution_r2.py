import math
import networkx as nx
from itertools import combinations

# Define the coordinates of cities including the depot
city_coords = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(i, j):
    x1, y1 = city_coords[i]
    x2, y2 = city_coords[j]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the graph representing all inter-city distances
G = nx.complete_graph(len(city_coords))
for i in range(len(city+s_coords)):
    for j in range(len(city_coords)):
        if i != j:
            G[i][j]['weight'] = calculate_distance(i, j)

# Christofides' Algorithm
def christofides_tsp(graph):
    # Step 1: Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    # Step 2: Find vertices of odd degree in the MST
    odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]
    # Step 3: Minimum Cost Perfect Matching
    odd_graph = nx.subgraph(graph, odd_degree_nodes)
    min_cost_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    # Add matching edges to MST
    mst.add_edges_from(min_cost_matching)
    # Step 4: Create Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(mst, source=0))
    # Make the circuit Hamiltonian by removing repeats
    visited = set()
    path = [0]  # Start at depot
    for u, v in euler_circuit:
        if v not in visited or v == 0:
            visited.add(v)
            path.append(v)
            if v == 0:
                break  # Close the tour at depot

    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(1, len(path)):
        total_cost += calculate_distance(path[i-1], path[i])

    return path, total_cost

# Solve the TSP
tour, total_cost = christofides_tsp(G)

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)