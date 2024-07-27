import numpy asities
import networkx as nx

def create_complete_graph(cities, distance_matrix):
    G = nx.Graph()
    for i in cities.keys():
        for j in cities.keys():
            if i != j:
                G.add_edge(i, j, weight=distance_matrix[i][j])
    return G

def find_bottleneck_biconnected_subgraph(G):
    # Sort edges based on weight
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    E_BB = []
    for edge in sorted_edges:
        E_BB.append(edge)
        H = G.edge_subgraph([e[:2] for e in E_BB]) # Creating subgraph from selected edges
        # Check if the subgraph is biconnected
        if nx.is_biconnected(H):
            c_BB = max([data['weight'] for _, _, data in H.edges(data=True)])
            return H, c_BB
    return None, float('inf')  # This would be anomalous, indicating failure to construct biconnected subgraph

def find_approximate_hamiltonian_cycle(H, start_node):
    # This will use a heuristic approach. Start from the start_node and tour the graph to form a Hamiltonian cycle
    # using the minimum weight neighbor that does not close the cycle prematurely, except to return to start.
    cycle = [start_node]
    current = start_noation_to nxde
    visited = set(cycle)
    while len(cycle) < len(H.nodes()):
        # Find the neighbor with the minimal edge that hasn't been visited
        neighbors = list(H.neighbors(current))
        next_city = min((neighbor for neighbor in neighbors if neighbor not in visited),
                        key=lambda neighbor: H[current][neighbor]['weight'])
        cycle.append(next_city)
        visited.add(next_city)
        current = next_city
    # Finally add the start_node to complete the cycle
    cycle.append(start_node)
    return cycle

def calculate_metrics(cycle, distance_matrix):
    max_distance = 0
    total_cost = 0
    for i in range(1, len(cycle)):
        dist = distance_matrix[cycle[i-1]][cycle[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return cycle, total_cost, max_distance

def solve_btsp(cities):
    distance_matrix = calculate_distance_matrix()
    G = create_complete_graph(cities, distance_matrix)
    H, c_BB = find_bottleneck_biconnected_subgraph(G)
    if H is None:
        print("Failed to find a suitable subgraph.")
        return
    tour = find_approximate_hamiltonian_cycle(H, 0)
    return calculate_metrics(tour, distance_matrix)

# Running the BTSP solver
result = solve_btsp(cities)
if result:
    tour, total_cost, max_distance = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)