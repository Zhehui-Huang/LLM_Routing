import networkx as nx
import math

# List of city coordinates, where index represents the city number
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def construct_graph():
    """Construct the full graph with cities as nodes and Euclidean distances as edge weights."""
    G = nx.Graph()
    num_cities = len(cles)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=distance)
    return G

def minimum_spanning_tree(G):
    """Calculate the minimum spanning tree of graph G."""
    return nx.minimum_spanning_tree(G, weight='weight')

def create_odd_degree_subgraph(G):
    """Create a subgraph of nodes of odd degree from graph G."""
    nodes = [v for v, d in G.degree() if d % 2 == 1]
    return G.subgraph(nodes)

def minimum_weight_perfect_matching(G, initial_matches=[]):
    """Calculate the minimum weight perfect matching for graph G (with possibly some initial matches)."""
    return nx.algorithms.matching.min_weight_matching(G, maxcardinality=True, weight='weight')

def eulerian_circuit(G, start):
    """Calculate an Eulerian circuit in graph G starting at node start."""
    return list(nx.eulerian_circuit(G, source=start))

def find_tour(path):
    """Converts Eulerian path to a valid TSP tour by skipping repeated nodes."""
    tour = []
    visited = set()
    for u, v in path:
        if u not in visited:
            tour.append(u)
            visited.add(u)
        if v not in visited:
            tour.append(v)
            visited.add(v)
    return tour

# Construct the graph
G = construct_graph()

# Compute the minimum spanning tree
mst = minimum_spanning_tree(G)

# Create subgraph of nodes with odd degree
odd_degree_subgraph = create_odd_degree_subgraph(mst)

# Compute the minimum weight perfect matching for odd-degree nodes
matching = minimum_weight_perfect_matching(odd_degree_subgraph)
matching_graph = nx.Graph()
matching_graph.add_edges_from(matching)

# Combine MST and matching graph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching_graph.edges())

# Find an Eulerian circuit in the combined graph
euler_circuit = eulerian_circuit(multi_graph, start=0)

# Convert Eulerian circuit to TSP tour
tour = find_tour(euler_circuit)

# Calculate total cost
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")