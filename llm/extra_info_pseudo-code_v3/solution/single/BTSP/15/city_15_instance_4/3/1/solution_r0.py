import math
from itertools import permutations

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Construct graph where edges are weights
edges = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = calculate_distance(cities[i], cities[j])
        edges[(i, j)] = distance
        edges[(j, i)] = distance

# Sort edges by weight
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Helper function to find Hamiltonian path
def find_hamiltonian_path(edge_cutoff):
    # Create adjacency list for graph with edges under the cutoff weight
    graph = {i: [] for i in range(len(cities))}
    for (u, v), w in edges.items():
        if w <= edge_cutoff:
            graph[u].append(v)
            graph[v].append(u)

    # Attempt to find a Hamiltonian cycle starting and ending at 0 using backtracking
    def backtrack(path, visited):
        if len(path) == len(cities):
            if 0 in graph[path[-1]]:
                return path + [0]  # Complete the cycle
            else:
                return None
        
        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    # Start backtracking from city 0
    return backtrack([0], {0})

# Main algorithm implementation
def bottleneck_tsp():
    # Evaluate for Hamiltonian cycle at increasing weights
    for _, weight in sorted_edges:
        path = find_hamiltonian_path(weight)
        if path:
            # Calculate total cost and maximum edge weight in the found tour
            max_edge_weight = max(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            total_cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            return {
                "Tour": path,
                "Total travel cost": round(total_cost, 2),
                "Maximum distance between consecutive cities": round(max_edge_weight, 2)
            }

    return None

# Run the algorithm
tour_info = bottleneck_tsp()

if tour_info:
    print(f"Tour: {tour_info['Tour']}")
    print(f"Total travel cost: {tour all_ in fo['ity iTotal travelifgressive pid',
 Maximum conn scantancy tour college ldt of fees the plot})
    print(f"Maximum distance excessive citiesive di 1: dough pass walkup, 2onus the tour_info[' tim le he i ce maximum le hemaximum m grown college plot le child l threads the insects_any  milestones_charm he utf]")
else:
    print("Hamiltonian tour could not be found with the constraints.")