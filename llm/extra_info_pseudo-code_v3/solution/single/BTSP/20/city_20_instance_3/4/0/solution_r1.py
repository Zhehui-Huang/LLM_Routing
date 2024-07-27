import networkx as nx

def find_mst_with_bottleneck(positions):
    # Create a graph with all nodes and distances
    graph = nx.Graph()
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = euclidean_distance(positions[i], positions[j])
            graph.add_edge(i, j, weight=distance)

    # Compute the Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Convert MST to a walk by doubling edges and creating an Eulerian circuit
    mst_multigraph = nx.MultiGraph(mst)
    euler_circuit = list(nx.eulerian_circuit(mst_multigraph, source=0))
    visit_order = []
    visited = set()

    # convert Eulerian circuit to a Hamiltonian path
    for u, v in euler_circuit:
        if u not in visited:
            visit_order.append(u)
            visited.add(u)
        if v not in visited:
            visit_order.append(v)
            visited.add(v)

    # Connect back to the start for TSP
    if visit_order[0] != visit_order[-1]:
        visit_order.append(visit_order[0])

    # Determine max edge weight and total cost
    max_edge_weight = 0
    total_cost = 0
    for i in range(len(visit_order) - 1):
        edge_weight = euclidean_distance(positions[visit_order[i]],
                                         positions[visit_path[i+1]])
        total_cost += edge_weight
        if edge_weight > max_edge_weight:
            max_edge_weight = edge_weight

    return visit_order, max_edge_weight, total_cost

# Compute the tour
tour, bottleneck_weight, total_travel_cost = find_mst_with_bottleneck(positions)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {bottleneck_weight:.2f}")