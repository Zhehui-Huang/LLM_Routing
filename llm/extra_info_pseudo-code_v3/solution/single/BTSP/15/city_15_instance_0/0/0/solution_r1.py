import math
from itertools import combinations

# Coordinates of the cities (including depot)
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including depot
n = len(cities)

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the matrix of distances
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]


# Function to check if a subset of edges can form a Hamiltonian cycle with the given max allowed distance
def can_form_hamiltonian_cycle(max_dist):
    # Create graph adjacency matrix where edges <= max_dist are marked 1
    adj = [[1 if distances[i][j] <= max_dist and i != j else 0 for j in range(n)] for i in range(n)]
    
    # Try to find a tour using backtracking
    path = [0]

    def visit(node):
        if len(path) == n:
            return adj[node][0] == 1  # The last city must connect to the depot
        
        for next_node in range(n):
            if adj[node][next_node] == 1 and next_node not in path:
                path.append(next_node)
                if visit(next_node):
                    return True
                path.pop()
        return False

    return visit(0)


# Solve the Bottleneck TSP
def solve_bottleneck_tsp():
    # Determine the low and high bounds of distances for binary search
    all_distances = sorted({distances[i][j] for i in range(n) for j in range(i + 1, n)})
    
    low, high = 0, len(all_distances) - 1
    while low < high:
        mid = (low + high) // 2
        max_dist = all_distances[mid]
        if can_form_hamiltonian_cycle(max_dist):
            high = mid
        else:
            low = mid + 1
    
    # The minimum maximum distance found
    optimal_max_dist = all_distances[high]
    
    # Construct the tour using the found maximum distance
    optimal_path = []
    included = [False] * n
    optimal_path.append(0)
    included[0] = True
    
    for _ in range(1, n):
        last = optimal_path[-1]
        for j in range(n):
            if not included[j] and distances[last][j] <= optimal_max_dist:
                optimal_path.append(j)
                included[j] = True
                break
    optimal_path.append(0)  # complete the cycle returning to the depot
    
    # Calculate the metrics for the found path
    total_cost = sum(distances[optimal_path[i]][optimal_path[i + 1]] for i in range(len(optimal_path) - 1))
    max_distance = max(distances[optimal_path[i]][optimal_path[i + 1]] for i in range(len(optimal_path) - 1))

    return optimal_path, total_cost, optimal_max_dist

# Using the Bottleneck TSP solver
tour, total_cost, max_distance = solve_bottleneck_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_behavior_research_dist}")