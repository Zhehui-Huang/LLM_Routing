import math
import networkx as nx

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Build a weighted graph based on given city coordinates
def build_graph(cities):
    G = nx.complete_graph(len(cities))
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            G[i][j]['weight'] = euclideanconv_distance(cities[i], cities[j])
    return G

# Identify an approximate optimal tour minimizing the maximum edge weight in the cycle
def find_tour(G):
    mst = nx.minimum_spanning_tree(G, weight='weight')  # Step 1: Start by MST
    multigraph = nx.MultiGraph()  # Step 2: Prepare for the double-tree approach
    multigraph.add_edges_from(mst.edges(data=True))
    multigraph.add_edges_from(mst.edges(data=True))

    # Make the graph Eulerian
    eulerian_graph = nx.eulerize(multigraph)

    # Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph))

    # Convert the Eulerian circuit to a Hamiltonian path (shortcutting)
    visited = set()
    hamiltonian_cycle = []
    max_edge_weight = 0
    last_visited = None

    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_cycle.append(u)
            if last_visited is not None:
                weight = G[last_visited][u]['weight']
                max_edge_weight = max(max_edge_weight, weight)
            last_visited = u

    # Close the cycle
    hamiltonian_cycle.append(hamiltonian_cycle[0])
    if last_visited is not None:
        weight = G[last_visited][hamiltonian_cycle[0]]['weight']
        max_edge_weight = max(max_edge_weight, weight)

    return hamiltonian_cycle, max_edge_weight

# Function to calculate tour metrics
def calculate_tour_metrics(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Main logic
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

G = build_graph(cities)
tour, bottleneck_weight = find_tour(G)
total_cost, max_consecutive_distance = calculate_tour_metrics(cities, tour)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)