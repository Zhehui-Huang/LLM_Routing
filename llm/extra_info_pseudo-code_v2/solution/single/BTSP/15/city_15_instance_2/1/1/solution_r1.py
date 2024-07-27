import math
import networkx as nx

# Data: Coordinates of the cities
locations = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(loc1, loc2):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

def create_complete_graph(locations):
    """ Constructs a complete graph from the given locations """
    G = nx.Graph()
    n = len(locations)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_inverse(loc1=locations[i], loc2=locations[j]))
    return G

def euclidean_inverse(loc1, loc2):
    """ Returns the inverse of the Euclidean distance to prioritize closer nodes in edge contraction """
    return 1 / euclidean_distance(loc1, loc2)

def construct_tour(G):
    """ Constructs an approximate optimal tour minimizing maximum distance between consecutive cities """
    mst = list(nx.minimum_spanning_edges(G, weight='weight'))
    biconnected_subgraph = nx.Graph(mst)

    while not nx.is_biconnected(biconnected_subgraph):
        weights = nx.get_edge_attributes(G, 'weight')
        edges_sorted = sorted(weights.items(), key=lambda x: x[1], reverse=True)
        for edge in edges_sorted:
            if edge not in biconnected_subgraph.edges():
                biconnected_subgraph.add_edge(*edge[0], weight=edge[1])
                if nx.is_biconnected(biconnected_subgraph):
                    break

    eulerian_tour = list(nx.eulerian_circuit(biconnected_subgraph))
    # Convert Eulerian tour to Hamiltonian path
    path = []
    visited = set()
    path_cost = 0
    previous = 0

    for u, v in eulerian_tour:
        if u not in visited:
            path.append(u)
            visited.add(u)
            if len(path) > 1:
                path_cost += euclidean_distance(locations[path[-2]], locations[u])

    path.append(path[0])  # complete the cycle
    path_cost += euclidean_distance(locations[path[-2]], locations[path[-1]])
    distances = [euclidean_distance(locations[path[i]], locations[path[i + 1]]) for i in range(len(path) - 1)]
    max_distance = max(distances)

    return path, path_cost, max_distance

# Main script execution
G = create_complete_graph(locations)
tour, total_cost, max_consec_distance = construct_tour(G)

# Output the results as requested
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consec_distance)