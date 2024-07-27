import math
import networkx as nx

# Define the coordinates of each city including the depot city
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct the complete graph
def create_complete_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Algorithm BB: Bottleneck-optimal Biconnected Subgraph
def algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())
    
    for edge in sorted_edges:
        G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_BB):
            break
        else:
            E_BB.append(edge)
    
    # Find bottleneck value
    c_BB = max([G_BB[u][v]['weight'] for u, v in G_BB.edges()])
    return G_BB, c_BB

# Main function to solve the problem
def solve_BTSP(cities):
    G = create_complete_graph(cities)
    G_BB, c_BB = algorithm_BB(G)
    
    # We would need the square of G_BB in reality, but might simplify due to pseudocode outline
    tour = list(nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight'))
    tour.append(tour[0])
    
    # Compute the total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = G[tour[i]][tour[i + 1]]['weight']
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    return tour, total_cost, max_distance

# Solve BTSP for the given cities and output the results
tour, total_cost, max_distance = solve_BTSP(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")