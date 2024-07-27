import math
from itertools import combinations

# Define the city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all edges with distances
edges = sorted([(i, j, distance(i, j)) for i in range(len(cities)) for j in range(i+1, len(cities))], key=lambda x: x[2])

# Simple implementation for ensuring biconnected subgraph and solving the problem
import networkx as nx

def find_tour(cities, edges):
    # Create graph
    G = nx.Graph()
    G.add_nodes_from(cities)
    
    # Algorithm BB to find bottleneck optimal biconnected subgraph
    E_BB = []
    G_BB = nx.Graph()
    G_BB.add_nodes_from(cities)
    
    for u, v, d in edges:
        G_BB.add_edge(u, v, weight=d)
        if nx.is_biconnected(G_BB):
            E_BB.append((u, v, d))
            break
        elif not nx.is_biconnected(G_BB):
            G_BB.remove_edge(u, v)
        else:
            E_BB.append((u, v, d))
    
    # Extra edges to ensure biconnected if break failed to provide it
    if not nx.is_biconnected(G_BB):
        for u, v, d in edges:
            if not G_BB.has_edge(u, v):
                G_BB.add_edge(u, v, weight=d)
                if nx.is_biconnected(G_BB):
                    break
    
    # Finding Hamiltonian path using approximation from biconnected subgraph
    T = list(nx.approximation.traveling_salesman_problem(G_BB, weight='weight', cycle=True))
    
    # Calculate the tour costs
    total_cost = sum(distance(T[i], T[i+1]) for i in range(len(T)-1))
    max_distance = max(distance(T[i], T[i+1]) for i in range(len(T)-1))
    
    return T, total_cost, max_distance

# Execute the function
tour, total_cost, max_distance = find_tour(cities, edges)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")