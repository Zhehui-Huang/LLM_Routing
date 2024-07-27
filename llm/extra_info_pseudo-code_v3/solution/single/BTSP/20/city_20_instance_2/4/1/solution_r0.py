import math
from itertools import permutations

# Cities coordinates with depot city 0 as the first entry
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    return [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

distance_matrix = create_distance_matrix(cities)

# Check if we can form a Hamiltonian cycle using the current edges
def is_hamiltonian_cycle_possible(edges, n):
    try:
        # Attempt a DFS to visit all nodes exactly once
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        visited_count = 0

        def dfs(node):
            nonlocal visited_count
            visited[node] = True
            visited_count += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Start DFS from node 0
        dfs(0)

        if visited_count != n:
            return False

        # Check if there's a path that returns to the starting node
        return any(0 in graph[i] for i in graph)
    except:
        return False

# Bottleneck TSP algorithm
def btsp_algorithm(distance_matrix):
    n = len(distance_matrix)
    edges = sorted((distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n))
    for weight, u, v in edges:
        # Check if a Hamiltonian cycle is possible with the current max distance edge
        possible_edges = [(i, j) for w, i, j in edges if w <= weight]
        if is_hamiltonian_cycle_possible(possible_edges, n):
            tour = [0]
            current = 0
            visited = [False] * n
            visited[current] = True
            while len(tour) < n:
                next_city = min((distance_matrix[current][i], i) for i in range(n) if not visited[i])[1]
                tour.append(next_city)
                visited[next_city] = True
                current = next_city
            tour.append(0)  # Return to the depot
            
            # Calculate the total cost and max cost
            total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            max_cost = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            return tour, total_cost, max_cost

# Execute the algorithm
tour, total_cost, max_cost = btsp_algorithm(distance_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_cost}")