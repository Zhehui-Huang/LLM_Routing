import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp(coordinates):
    n = len(coordinates)
    graph = {i: {} for i in range(n)}
    
    # Create a complete graph in terms of distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            graph[i][j] = dist
            graph[j][i] = dist
    
    # Use NetworkX to construct the graph
    G = nx.Graph()
    for i in graph:
        for j in graph[i]:
            G.add_edge(i, j, weight=graph[i][j])
    
    # Using the minimum spanning tree as a subgraph to start with, followed by adding edges until biconnected
    mst = nx.minimum_spanning_tree(G)
    max_edge_in_mst = max(e[2]['weight'] for e in mst.edges(data=True))
    
    # Attempt to make the graph biconnected while minimizing the bottleneck
    bcc = nx.minimum_edge_cut(G)
    for edge in bcc:
        mst.add_edge(*edge, weight=G[edge[0]][edge[1]])

    max_bottleneck = max(max_edge_in_mst, max(G[edge[0]][edge[1]] for edge in bcc))
    
    # Use the approximated subgraph to find a Hamiltonian cycle closest to TSP solution
    # Basic heuristic:nearest neighbor or Christofides algorithm  
    from networkx.algorithms.approximation import traveling_salesman_problem
    tsp_tour = traveling_salesman_problem(mst, cycle=True, weight='weight')
    
    # Calculate tour details    
    tour_cost = sum(G[tsp_tour[i]][tsp_tour[i + 1]]['weight'] for i in range(len(tsp_tour) - 1))
    max_dist_consec_cities = max(G[tsp_tour[i]][tsp_tour[i + 1]]['weight'] for i in range(len(tsp_tour) - 1))

    return tsp_tour, tour_cost, max_dist_consec_cities


# City locations
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

tour, total_cost, max_distance = solve_tsp(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2fi}")