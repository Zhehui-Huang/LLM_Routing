import itertools
import math

# City coordinates
coordinates = [
    (35, 40),  # City 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all distance pairs and store them
num_cities = len(coordinates)
edges = []
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            edges.append((i, j, distance(coordinates[i], coordinates[j])))

# Sort edges by distance
edges.sort(key=lambda x: x[2])

def can_form_hamiltonian_path(cutoff_distance):
    # Create adjacency list for the subgraph with edge distances <= cutoff_distance
    adjacency_list = {i: [] for i in range(num_cities)}
    for (a, b, d) in edges:
        if d <= cutoff_distance:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

    # Try to find any Hamiltonian path starting at city 0 using backtracking
    def hamiltonian_path(v, visited, path):
        if len(path) == num_cities:
            if path[-1] == 0:  # path must end at the depot city
                return path
            return None
        for neighbor in adjacency_layout[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                result = hampath(neighbor, visited, path)
                if result is not None:
                    return result
                visited.remove(neighbor)
                path.pop()
        return None

    return hamiltonian_path(0, {0}, [0])

# Main algorithm to find the bottleneck Hamiltonian path
def bottleneck_tsp():
    for cutoff_distance in edges:
        result = can_form_hamiltonian_path(cutoff_distance[2])
        if result is not None:
            max_dist = cutoff_distance[2]
            return result, sum(distance(coordinates[result[i]], coordinates[result[i + 1]]) for i in range(len(result) - 1)), max_dist

# Run the algorithm
tour, total_cost, max_distance = bottleneck_tsp()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)