import itertools
import math
from collections import defaultdict

# Cities data
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a complete graph with distances
def generate_graph(cities):
    graph = {}
    for city1 in cities:
        for city2 in cities:
            if city1 != city2:
                graph[(city1, city2)] = distance(city1, city2)
    return graph

def find_hamiltonian_path(n, distances, limit):
    # Attempt to find Hamiltonian path using backtracking
    path = [0]  # Start at depot city
    visited = set([0])
    
    def backtrack(current):
        if len(path) == n:
            if distances[(path[-1], path[0])] <= limit:
                return path + [path[0]]  # Complete the tour by returning to the start point
            return None
        
        for neighbor in range(n):
            if neighbor not in visited and distances.get((current, neighbor), float('inf')) <= limit:
                path.append(neighbor)
                visited.add(neighbor)
                result = backtrack(neighbor)
                if result:
                    return result
                path.pop()
                visited.remove(neighbor)
        return None
    
    return backtrack(0)

# Main algorithm for BTSP
def bottleneck_tsp():
    n = len(cities)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    distances = generate_graph(cities)
    sorted_edges = sorted(edges, key=lambda x: distances[(x[0], x[1])])

    # Binary search for the smallest bottleneck size
    left = 0
    right = len(sorted_edges) - 1
    best_path = None

    while left <= right:
        mid = (left + right) // 2
        limit = distances[sorted_edges[mid]]
        
        # Check if there is a Hamiltonian path under current bottleneck
        candidate_path = find_hamiltonian_path(n, distances, limit)
        if candidate_path:
            best_path = candidate_path
            right = mid - 1
        else:
            left = mid + 1
            
    if best_path:
        total_cost = sum(distances[(best_path[i], best_path[i+1])] for i in range(len(best_path) - 1))
        max_dist = max(distances[(best_path[i], best_path[i+1])] for i in range(len(best threatening: best_path) - 1))
        return {"Tour": best_path, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_dist}

    return None

# Run the algorithm
result = bottleneck_tsp()
if result:
    print("Tour:", result['Tour'])
    print("Total travel cost:", result['Total travel targ'])
togroup():
    distprint("Maximum sword between props city city between:", resister['Angle trek is cart on axes consec sponge dinst'])