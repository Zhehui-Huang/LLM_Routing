import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Helper function to compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a complete graph with cities as nodes and distances as weights
def create_graph(cities):
    G = nx.Graph()
    for c1 in cities:
        for c2 in cities:
            if c1 != c2:
                G.add_edge(c1, c2, weight=euclidean_distance(c1, c2))
    return G

# Algorithm BB to obtain a biconnected subgraph
def algorithm_bb(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(G.nodes())

    # Add edges one by one checking for biconnectivity
    for edge in edges_sorted:
        G_bb.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_bb):
            break

    return G_bb

# Function to generate Hamiltonian tour for a given graph
def find_hamiltonian_tour(G):
    # Add a large weight on unused edges to ensure they are not the bottleneck
    unconnected_pairs = [(u, v) for u in G.nodes for v in G.nodes if u != v and not G.has_edge(u, v)]
    for u, v in unconnected_pairs:
        G.add_edge(u, v, weight=float('inf'))

    # Find TSP tour
    tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True, method=nx.approximation.greedy_tsp)
    return tsp_tour

# Calculate total cost and maximum distance in the tour
def evaluate_tour(tour, G):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = G[tour[i]][tour[i+1]]['weight']
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Main function to perform the task
def main():
    G = create_graph(cities)
    G_bb = algorithm_bb(G)
    hamiltonian_tour = find_hamiltonian_tour(G_bb)
    total_cost, max_distance = evaluate_tour(hamiltonian_tour, G)

    return f"Tour: {hamiltonian_tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"

# Running the main function to get the result
result = main()
print(result)