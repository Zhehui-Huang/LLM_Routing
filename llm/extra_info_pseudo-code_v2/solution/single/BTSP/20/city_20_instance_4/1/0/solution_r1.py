import math
import networkx as nx

# City coordinates including the depot
city_coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(idx1, idx2):
    (x1, y1), (x2, y2) = city_coords[idx1], city_coords[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def create_complete_graph(n, city_coords):
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(i, j))
    return G

def minimal_biconnected_subgraph(G):
    edges_sorted_by_weight = sorted(G.edges(data='weight'), key=lambda item: item[2])
    B = nx.Graph()

    for edge in edges_sorted_by_weight:
        B.add_edge(edge[0], edge[1], weight=edge[2])
        if nx.is_biconnected(B):
            max_weight = max((B[u][v]['weight'] for u, v in B.edges()))
            return B, max_weight
    return None, float('inf')  # Should not happen, as we will find a biconnected subgraph

def find_hamiltonian_cycle(B):
    # For demonstration, using simple heuristics as the problem is NP-hard
    return list(nx.approximation.traveling_salesman_problem(B, cycle='greedy'))

def tour_metrics(tour, city_coords):
    max_distance = 0
    total_distance = 0
    tour_complete = tour + [tour[0]]  # Return to starting point

    for i in range(len(tour)):
        dist = euclidean_distance(tour_complete[i], tour_complete[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    return tour_complete, total_distance, max_distance

# Initialize graph, apply algorithms
n = len(city_coords)
G = create_complete_graph(n, city_coords)
B, max_edge_weight = minimal_biconnected_subgraph(G)
tour = find_hamiltonian_cycle(B)

# Calculate the required metrics
tour_complete, total_distance, max_distance = tour_metrics(tour, city_coords)

# Display results
print(f"Tour: {tour_complete}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")