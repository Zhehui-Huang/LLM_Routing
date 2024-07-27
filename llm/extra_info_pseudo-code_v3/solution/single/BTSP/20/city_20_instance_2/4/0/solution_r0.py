import math
import itertools

# Coordinates of cities including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute distances between all pairs of cities
distances = {}
for i in range(20):
    for j in range(i+1, 20):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Bottleneck Traveling Salesman Problem Solution
def find_bottleneck_tsp():
    # Create sorted list of unique distances
    unique_distances = sorted(set(distances.values()))
    
    # Check for a Hamiltonian cycle within each unique distance
    for max_edge_length in unique_distances:
        # Create graphs with edges only if the distance <= max_edge_length
        edges = [(a, b) for (a, b), d in distances.items() if d <= max_edge_length]
        
        # Perform a DFS based search for each potential starting point to find a Hamiltonian cycle
        for start in range(20):
            if find_hamiltonian_cycle(edges, start, max_edge_length):
                max_edge_cost = max_edge_length
                return tour, total_cost, max_edge_cost
    return [], float('inf'), float('inf')

def find_hamiltonian_cycle(edges, start, max_length):
    # Using backtracking to find a Hamiltonian cycle
    path = [start]
    def backtrack(current, visited):
        if len(path) == 20 and (path[0], path[-1]) in edges:
            # Calculate the tour statistics
            total_cost = sum(distances[path[i], path[i+1]] for i in range(19))
            total_cost += distances[path[-1], path[0]]  # closing the loop
            global tour
            tour = path + [path[0]]
            return True, total_cost
        
        for (u, v) in edges:
            if u == current and v not in visited and (path + [v] if len(path) == 19 else True):
                path.append(v)
                visited.add(v)
                if backtrack(v, visited)[0]:
                    return True
                path.pop()
                visited.remove(v)
    
    _, total_cost = backtrack(start, {start})
    return tour, total_cost

tour, total_cost, max_edge_cost = find_botleneck_tsp()

# Output the required information
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_cost:.2f}")