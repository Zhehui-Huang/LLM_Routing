import math
import itertools

# City coordinates
cities = [
    (90, 3),   # City 0 (depot)
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_hamiltonian_path_bottleneck(cities, max_edge_weight):
    """ Given a max_edge_weight, construct a graph and try finding a Hamiltonian path using backtracking. """
    n = len(cities)
    graph = [[0]*n for _ in range(n)]
    
    # Create adjacency matrix with edges weights <= max_edge_weight
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            if dist <= max_edge_weight:
                graph[i][j] = graph[j][i] = 1
            else:
                graph[i][j] = graph[j][i] = 0

    # Try to find Hamiltonian Cycle starting and ending at the depot (0)
    path = [0]
    used = [False] * n
    used[0] = True

    def backtrack(node):
        if len(path) == n:
            return graph[path[-1]][0] == 1  # check if last node connects back to depot
            
        for v in range(1, n):
            if not used[v] and graph[node][v] == 1:
                used[v] = True
                path.append(v)
                if backtrack(v):
                    return True
                path.pop()
                used[v] = False
        return False
    
    if backtrack(0):
        path.append(0)  # complete the cycle
        return path
    return None

# Main function to solve the BTSP
def solve_btsp(cities):
    # Generate all possible edges and sort them by weight
    edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in range(len(cities)) for j in range(i+1, len(cities))]
    edges.sort(key=lambda x: x[2])
    
    # Try to find a Hamiltonian cycle starting from the smallest possible maximum edge
    for _, _, max_edge_weight in edges:
        hamiltonian_path = find_hamiltonian_path_bottleneck(cities, max_edge_weight)
        if hamiltonian_path:
            # Calculate the total cost and max distance in the path
            max_distance = 0
            total_cost = 0
            for i in range(1, len(hamiltonian_path)):
                dist = euclidean_distance(cities[hamiltonian_path[i-1]], cities[hamiltonian_path[i]])
                total_cost += dist
                if dist > max_distance:
                    max_distance = dist
            return {
                "Tour": hamiltonian_path,
                "Total travel cost": total_cost,
                "Maximum distance between consecutive cities": max_distance
            }
    return None

# Execute
output = solve_btsp(cities)
print(f"Tour: {output['Tour']}")
print(f"Total travel cost: {output['Total travel cost']}")
print(f"Maximum distance between consecutive cities: {output['Maximum distance between consecutive cities']}")