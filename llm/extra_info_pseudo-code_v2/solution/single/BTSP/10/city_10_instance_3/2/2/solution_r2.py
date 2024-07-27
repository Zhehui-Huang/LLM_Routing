import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def build_biconnected_subgraph(cities):
    n = len(cities)
    edges = [(i, j, euclidean_distance(cities[i], cities[j]))
             for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])

    from networkx import Graph, is_biconnected
    G = Graph()
    G.add_nodes_from(range(n))
    
    # Add edges by increasing weight until the graph is biconnected
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        if is_biconnected(G):
            break

    return G

def find_approximate_tour(G, start_node=0):
    # Since exact Hamiltonian path finding is NP, we create a MST-based path
    from networkx import approximations
    mst = approximations.minimum_spanning_tree(G, weight='weight')
    mst.add_edge(0, 0)  # To allow a tour
    tour = list(approximations.traveling_salesman_problem(mst, nodes=mst.nodes(), cycle=True, weight='weight'))
    
    # Make sure to start at the start_node
    while tour[0] != start_node:
        tour.append(tour.pop(0))
    tour.append(start_node)  
    
    return tour

# Define the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Construct a biconnected subgraph
G_BB = build_biconnected_subgraph(cities)

# Find an approximate tour
tour = find_approximate_tour(G_BB)

# Calculate tour costs
total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
max_travel_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_travel_distance:.2f}")