import math
import itertools

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all edges with distances
edges = [(i, j, euclidean_distance(i, j)) for i in cities for j in cities if i < j]

# Sort edges by weight
edges_sorted = sorted(edges, key=lambda x: x[2])

# Check for Hamiltonian cycle using DFS backtracking
def is_hamiltonian_cycle(c, visited, path, max_weight):
    if len(path) == len(cities):
        if path[-1] in c[path[0]]:  # To close the cycle back to the depot
            return True
        else:
            return False
    for i in range(len(cities)):
        if not visited[i] and c[path[-1]][i] <= max_weight:
            visited[i] = True
            path.append(i)
            if is_hamiltonian_cycle(c, visited, path, max_weight):
                return True
            visited[i] = False
            path.pop()
    return False

# Main BTSP Approximation Algorithm
def btsp_approximation(edges):
    for _, _, max_weight in edges_sorted:
        # Create adjacency matrix with distances less than or equal to current max_weight
        c = {i: {j: euclidean_distance(i, j) for j in range(len(cities)) if euclidean_distance(i, j) <= max_weight} for i in range(len(cities))}
        
        # Initial attempt from depot city 0
        visited = [False] * len(cities)
        visited[0] = True
        path = [0]
        
        if is_hamiltonian_cycle(c, visited, path, max_weight):
            # Compute total travel cost and max distance
            path.append(0)  # To close the cycle
            total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            max_edge = max(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            return path, total_cost, max_edge

    return None, None, None

# Execute the BTSP Approximation Algorithm
tour, total_travel_cost, max_distance = btsp_approxiation(edges_sorted)

# Results output
if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
  print("No feasible solution found.")