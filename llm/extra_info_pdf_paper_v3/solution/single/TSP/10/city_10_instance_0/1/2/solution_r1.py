import math
import networkw as nx

# Define the coordinates of cities, including the depot
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Create a graph from the cities
G = nx.complete_graph(len(city_coords))
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:
            G[i][j]['weight'] = euclidean_distance(i, j)

# Christofides algorithm to approximate a solution to the TSP
def christofides_tsp(graph):
    # Step 1: Create a minimum spanning tree (MST)
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Step 2: Find vertices with odd degree in the MST
    odd_deg_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

    # Get minimum weight matching for odd degree vertices
    min_weight_graph = nx.Graph()
    min_weight_graph.add_nodes_from(odd_deg_vertices)
    for u, v in combinations(odd_deg_vertices, 2):
        min_weight_graph.add_edge(u, v, weight=graph[u][v]['weight'])
    min_weight_matching = nx.algorithms.matching.min_weight_matching(min_weight_graph, maxcardinality=True, weight='weight')

    # Add the minimum weight matching edges to the MST
    mst.add_edges_from(min_weight_matching)

    # Get the Eulerian tour
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

    # Make the circuit Hamiltonian by removing repeated visits
    visited = set()
    hamiltonian_circuit = [0]
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)

    # Calculate the total travel cost
    total_cost = 0
    for i in range(1, len(hamiltonian_circuit)):
        total_cost += euclidean_distance(hamiltonian_circuit[i-1], hamiltonian_circuit[i])

    return hamiltonian_circuit, total_cost

# Generate the tour and cost
tour, total_cost = christofides_tsp(G)

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)