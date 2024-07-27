import math
import itertools
from sys import float_info

# Define the cities with their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    dx = city1[0] - city2[0]
    dy = city1[1] - city2[1]
    return math.sqrt(dx * dx + dy * dy)

# Generate all distances between cities
def all_distances(cities):
    num_cities = len(cities)
    dist = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist[i][j] = calc_distance(cities[i], cities[j])
            else:
                dist[i][j] = float('inf')  # Distance from a city to itself is infinite    
    return dist

# Find an approximate optimal BTSP tour
def approximate_optimal_tour(cities):
    distances = all_distances(cities)
    N = len(cities)
    # Use iterated closest pair strategy to construct initial biconnected subgraph
    sorted_edges = sorted((distances[i][j], i, j) 
                          for i in range(N) for j in range(N) if i != j)
    
    # Initialize a disjoint set data structure to manage connected components
    parent = list(range(N))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            
    # Building the biconnected subgraph
    edge_count = 0
    E_BB = []
    subgraph_max = 0
    
    for d, i, j in sorted_edges:
        if find(i) != find(j):
            union(i, j)
            E_BB.append((i, j))
            edge_count += 1
            subgraph_max = max(subgraph_max, d)
            if edge_count == N-1:
                break
    
    # Constructing a tour from biconnected subgraph
    tour = [0]
    visited = [False] * N
    visited[0] = True
    
    def visit(current):
        if all(visited):
            return [0]
        possible_moves = [j for d, i, j in E_BB if i == current and not visited[j]]
        possible_moves.sort(key=lambda x: distances[current][x])
        for move in possible_a:
            visited[move] = True
            rest_of_tour = visit(move)
            if rest_of_tour:
                return [move] + rest_of_tour
            visited[move] = False
        return []
    
    complete_tour = [0] + visit(0)
    
    # Calculate the costs required by format
    total_cost = sum(distances[complete_tour[i]][complete_tour[i+1]] for i in range(len(complete_tour)-1))
    max_cost = max(distances[complete_tour[i]][complete_tour[i+1]] for i in range(len(complete_tour)-1))
    
    return complete_tour, total_cost, max_cost

# Run the algorithm
tour, total_cost, max_distance = approximate_optimal_tour(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")