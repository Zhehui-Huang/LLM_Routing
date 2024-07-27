import math
from itertools import permutations

# Given cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Form all possible edges with their weights
edges = [(i, j, distance(i, j)) for i in range(20) for j in range(i+1, 20)]
edges.sort(key=lambda x: x[2]) # Sort edges by weight

def find(C, x):
    if C[x] != x:
        C[x] = find(C, C[x])
    return C[x]

def union(C, r1, r2):
    C[r1] = r2

def check_hamiltonian_path(V, max_length):
    # Brute-force checking for Hamiltonian path using backtracking, limited by max_length
    n = len(V)
    visited = [False] * n
    
    def backtrack(current_node, count_visited, path):
        if count_visited == n:
            return path + [V[0]]

        for j in range(n):
            if not visited[j] and distance(V[current_node], V[j]) <= max_length:
                visited[j] = True
                res = backtrack(j, count_visited+1, path + [V[j]])
                if res:
                    return res
                visited[j] = False
        return False
            
    # Start from the depot city, index 0 assumed as city 0
    visited[0] = True
    return backtrack(0, 1, [V[0]])

for w in edges:
    max_edge_length = w[2]
    # Generate the threshold graph with max_edge_length
    threshold_graph = [e for e in edges if e[2] <= max_edge_length]
    if len(threshold_graph) < 19:  # At least n-1 edges needed to consider forming a path
        continue
    
    # Check if a Hamiltonian path exists
    path = check_hamiltonian_path(list(range(20)), max_edge_length)
    
    if path:
        max_dist = max(distance(path[i], path[i+1]) for i in range(len(path)-1))
        total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
        break