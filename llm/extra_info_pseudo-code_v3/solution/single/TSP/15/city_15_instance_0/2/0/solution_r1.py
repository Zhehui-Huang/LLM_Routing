import math
import networkx as nx
import itertools
import networkx.algorithms.approximation as nx_approx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_graph(city_positions):
    G = nx.Graph()
    num_cities = len(city_positions)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=euclidean_distance(city_positions[i], city_positions[j]))
    return G

def minimum_weight_perfect_matching(G, odd_vertices):
    # nx.max_weight_matching computes a maximum weight matching
    # We convert it to a minimum by converting weights to negative, matching, and then inverting again.
    # Since networkx assumes maximum weight, we need to negate weights for a "Min-Cost" perfect matching perspective
    modified_graph = nx.Graph()
    for u, v, d in G.edges(data=True):
        modified_graph.add_edge(u, v, weight=-d['weight'])

    matching_edges = nx.algorithms.max_weight_matching(modified_graph, maxcardinality=True)

    matching_graph = nx.Graph()
    for e in matching_edges:
        u, v = e
        matching_graph.add_edge(u, v, weight=-modified_graph[u][v]['weight'])

    return matching_graph

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def christofides_algorithm(city_positions):
    G = create_graph(city_positions)
    T = nx.minimum_spanning_tree(G)
    odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]

    # Subgraph induced by odd degree vertices
    subgraph = G.subgraph(odd_degree_vertices)
    M = minimum_weight_perfect_matching(G, odd_degree_vertices)

    # Combine the edges of T (MST) and M (perfect matching)
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M.edges())

    # Find an eulerian circuit:
    eulerian_circuit = find_eulerian_circuit(multigraph)

    # Convert the Eulerian circuit to Hamiltonian circuit
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    
    tour.append(tour[0])  # Return to the depot

    # Calculate the tour cost
    tour_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

    return tour, tour_cost

# Define city positions (index corresponds to city number)
city_positions = [
    (9, 93),  # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Compute the tour and cost
tour, cost = christofides_algorithm(city_positions)

print("Tour: ", tour)
print("Total travel cost: {:.2f}".format(cost))