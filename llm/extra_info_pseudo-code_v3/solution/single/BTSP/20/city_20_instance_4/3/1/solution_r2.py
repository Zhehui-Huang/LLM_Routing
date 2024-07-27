import math
import itertools
from sys import maxsize as inf

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Cities (index: (x, y))
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute distances between all city pairs
distances = [[euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1]) for j in range(20)] for i in range(20)]

# Building the graph dynamically
edges = [(i, j) for i in range(20) for j in range(20) if i != j]

# Approximating the TSP solution via the Bottleneck approach
def bottleneck_tsp():
    sorted_edges = sorted(edges, key=lambda x: distances[x[0]][x[1]])
    best_path = []
    best_max_dist = inf
    
    # Check each edge weight threshold if it forms a valid tour
    for threshold in sorted(set(distances[i][j] for i, j in edges)):
        subgraph = {i: [] for i in range(20)}
        for i, j in sorted_edges:
            if distances[i][j] <= threshold:
                subgraph[i].append(j)
                subgraph[j].append(i)
        
        # Using DFS to find a Hamiltonian cycle
        visited = [False] * 20
        path = []
        
        def dfs(v, count):
            visited[v] = True
            path.append(v)
            if count == 20:
                return path[0] in subgraph[path[-1]]
            for next_v in subgraph[v]:
                if not visited[next_v]:
                    if dfs(next_v, count + 1):
                        return True
            visited[v] = False
            path.pop()
            return False
        
        if dfs(0, 1):
            best_path = path + [path[0]]
            best_max_dist = threshold
            break
    
    total_distance = sum(distances[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))
    result = {
        'Tour': best_path,
        'Total travel cost': total_distance,
        'Maximum distance between consecutive cities': best_max_dist
    }
    return result

# Execute the function
result = bottleneck_tsp()

# Output the results
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutiveWow, city}:.2f}")