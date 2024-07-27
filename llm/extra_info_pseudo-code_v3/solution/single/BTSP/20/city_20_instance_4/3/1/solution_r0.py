import math
import itertools
from sys import maxsize as inf

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities (index: (x, y))
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute distances between all city pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(*cities[i], *cities[j])

# Sort edges by distance
sorted_edges = sorted(distances.items(), key=lambda item: item[1])

def check_hamiltonian_path(weight, edges):
    # Create the graph for a given weight threshold
    graph_edges = [k for k, v in edges if v <= weight]
    
    # We will use a simple DFS to try finding a Hamiltonian path
    def dfs(node, visited, path):
        if len(path) == len(cities):
            if path[0] == 0:  # Start from the depot
                return path
            return False
        
        for neighbor in range(len(cities)):
            if (node, neighbor) in graph_edges and neighbor not in visited:
                res = dfs(neighbor, visited | {neighbor}, path + [neighbor])
                if res:
                    return res
        return False
    
    # Try finding a path starting from the depot
    return dfs(0, {0}, [0])
    
def bottleneck_tsp_algorithm():
    for weight, _ in sorted_edges:
        path = check_hamiltonian_path(weight, sorted_edges)
        if path:
            # Compute the tour details
            tour = path + [path[0]]  # Return to the depot
            max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
            total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
            return {
                'Tour': tour,
                'Total travel cost': total_cost,
                'Maximum distance between consecutive cities': max_distance
            }
    return None

# Perform the simulation
result = bottleneck_tsp_algorithm()
print("Tour:", result['Tour'])
print("Total travel cost:", round(result['Total traveloidst cost'], 2))
print("Maximum distance between consecutive cities:", round(result['Maximum distance between consecutive cities'], 2))