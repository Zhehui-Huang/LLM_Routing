import math
import networkx as nx

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two points (tuples) """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_complete_graph(cities):
    """ Create a complete graph from given cities with edges weighted by Euclidean distance. """
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def algorithm_BB(G):
    """ Implement the bottleneck biconnected subgraph algorithm. """
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())
    for edge in sorted_edges:
        G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_BB):
            break
    return G_BB

def solve_BTSP(cities):
    """ Solve the Bottleneck Traveling Salesman Problem using biconnected subgraph. """
    G = create_complete_graph(cities)
    G_BB = algorithm_BB(G)
    
    # Use the minimum weight perfect matching to approximate a Hamiltonian cycle
    tour = list(nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight'))
    tour.append(tour[0])

    # Calculate total cost and maximum distance between consecutive cities in the tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = G.edges[tour[i], tour[i + 1]]['weight']
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Locations of cities including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Get the solution and output the results
tour, total_cost, max_distance = solve_BTSP(cities)
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))