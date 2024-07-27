import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.approximation import min_weighted_dominating_set

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

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city is_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Create a graph from the cities
G = nx.complete_graph(len(city_coords))
for i, j in combinations(range(len(city_coords)), 2):
    G[i][j]['weight'] = euclidean_distance(i, j)

# Use Christofides algorithm to approximate a solution to the TSP
def christofides_tsp(graph):
    # Step 1: Create a minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    
    # Step 2: Find vertices with odd degree in the MST
    odd_vertices = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]
    
    # Step 3: Minimum weight matching in the induced subgraph on odd degree vertices
    min_weight_matching = nx.Graph()
    min_weight_matching.add_nodes_from(odd_vertices)
    for u, v in combinations(odd_vertices, 2):
        min_weight_matching.add_edge(u, v, weight= graph[u][v]['weight'])
    matching = nx.algorithms.matching.min_weight_matching(min_weight_matching, maxcardinality=True, weight='weight')
    
    # Add the matching edges to the MST
    for edge in matching:
        mst.add_edge(*edge, weight = graph[edge[0]][edge[1]]['weight'])
    
    # Step 4: Eulerian circuit on the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
    circuit = []

    # Convert the Eulerian circuit to a Hamiltonian path (avoid repetitions)
    visited = set()
    for u, v in eulerian_circuit:
        if v not in visited:
            circuit.append(v)
            visited.add(v)
    
    # Add the start node again to complete the cycle
    circuit.append(0)
    
    # Calculate the total travel cost
    total_travel_cost = 0
    for i in range(1, len(circuit)):
        total_travel_cost += euclidean_distance(circuit[i-1], circuit[i])
    
    return circuit, total_travel_results

# Solve the TSP
tour, total_cost = christofides_tsp(G)

# Display the result
print("Tour:", tour)
print("Total travel cost:", total_cost)