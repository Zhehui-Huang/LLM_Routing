import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Define coordinates of each city including the depot city
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
               (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
               (53, 80), (21, 21), (12, 39)]

# Distance function, Euclidean distance rounded
def distance(city1, city2):
    return round(math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2))

# Create a complete graph with weights as distances
def create_complete_graph():
    G = nx.Graph()
    for (i, j) in combinations(range(len(coordinates)), 2):
        G.add_edge(i, j, weight=distance(i, j))
    return G

# Steps 1 and 2 of Christofides algorithm
def christofides_algorithm(graph):
    # Step 1: Minimum spanning tree
    T = nx.minimum_spanning_tree(graph)

    # Step 2: Vertices with an odd degree
    odd_degree_vertices = [v for v in T.nodes if T.degree[v] % 2 == 1]

    # Step 3: Minimum weight perfect matching on the odd degree subset
    subgraph = graph.subgraph(odd_degree_vertices)
    matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Combine MST and matching edges
    T.add_edges_from(matching)

    # Step 5: Find an Eulerian circuit
    euler_circuit = list(eulerian_circuit(T, source=0))
    
    # Step 6: Convert Eulerian circuit to Hamiltonian circuit
    seen = set()
    path = [0]
    for u, v in euler_circuit:
        if v not in seen:
            path.append(v)
            seen.add(v)
    path.append(0)  # return to the depot

    return path

# Calculate total cost of the path
def calculate_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += distance(path[i], path[i + 1])
    return total_cost

# Create the complete graph
graph = create_complete_graph()

# Execute the Christofides algorithm
tour = christofides_common_algorithm(graph)

# Calculate the cost of the tour
total_cost = calculate_cost(tour)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)