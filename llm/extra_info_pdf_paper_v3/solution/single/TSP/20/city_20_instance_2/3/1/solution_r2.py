import math
import networkx as nx

# Given coordinates of cities including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
    (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_graph(coordinates):
    """Create a fully connected graph with Euclidean distances as edge weights."""
    G = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))
    return G

def find_minimum_spanning_tree(G):
    """Return the Minimum Spanning Tree of a given graph."""
    return nx.minimum_spanning_tree(G, weight='weight')

def get_odd_degree_vertices(G):
    """Return a list of nodes with odd degree in graph G."""
    return [v for v, d in G.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    """Find minimum weight perfect matching for a subgraph induced by odd degree nodes."""
    odd_subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

def combine_graphs(MST, matching):
    """Combine edges from MST and matching into a single graph to form an Eulerian trail."""
    G = nx.MultiGraph(MST)
    G.add_edges_from(matching)
    return G

def eulerian_circuit_to_hamiltonian_circuit(G, start_node):
    """Convert an Eulerian circuit to a Hamiltonian circuit by shortcutting already visited nodes."""
    seen = set()
    circuit = []
    for u, v in nx.eulerian_circuit(G, source=start_node):
        if u not in seen:
            circuit.append(u)
            seen.add(u)
    circuit.append(start_node)  # to return to the starting node
    return circuit

def calculate_tour_cost(G, tour):
    """Calculate total tour cost based on the provided tour."""
    return sum(G[u][v][0]['weight'] for u, v in zip(tour[:-1], tour[1:]))

# Running the algorithm
G = create_distance_graph(coordinates)
MST = find_minimum_spanning_tree(G)
odd_vertices = get_odd_degree_vertices(MST)
matching = minimum_weight_perfect_matching(G, odd_vertices)
eulerian_graph = combine_graphs(MST, matching)
circuit = eulerian_circuit_to_hamiltonian_circuit(eulerian_graph, 0)
tour_cost = calculate_tour_cost(G, circuit)

# Output results
print("Tour:", circuit)
print("Total travel cost:", round(tour_cost, 2))