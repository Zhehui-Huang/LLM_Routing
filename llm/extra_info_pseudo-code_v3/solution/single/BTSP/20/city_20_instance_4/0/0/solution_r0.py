import math
from itertools import permutations

# Data for the cities
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Get all edges with their distances
edges = []
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            edges.append((city1, city2, calculate_distance(city1, city2)))

# Sort edges by distance
edges.sort(key=lambda x: x[2])

# Set of all cities
all_cities = set(cities.keys())

# Function to check if there is a Hamiltonian path given a graph
def has_hamiltonian_path(graph, start_city):
    def visit(city, visited):
        visited.add(city)
        if len(visited) == len(all_cities):
            return True
        for neighbor in graph[city]:
            if neighbor not in visited and visit(neighbor, visited):
                return True
        visited.remove(city)
        return False

    return visit(start_city, set())

# Heuristic to find tour by bottleneck limitation
def find_bottleneck_tour():
    for _, _, max_distance in edges:
        subgraph = {city: [] for city in cities}
        for city1, city2, distance in edges:
            if distance <= max_distance:
                subgraph[city1].append(city2)
                subgraph[city2].append(city1)
        if has_hamiltonian_path(subgraph, 0):
            # Construct path based on max_distance still respecting the cities transitions
            path = [0]
            visited = set([0])
            current_city = 0
            while len(visited) != len(cities):
                for neighbor in sorted(subgraph[current_city]):
                    if neighbor not in visited:
                        path.append(neighbor)
                        visited.add(neighbor)
                        current_city = neighbor
                        break
            path.append(0)  # returning to depot
            break
    
    max_edge_distance = 0
    total_distance = 0
    for i in range(len(path) - 1):
        dist = calculate_distance(path[i], path[i + 1])
        total_distance += dist
        if dist > max_edge_distance:
            max_edge_distance = dist

    return path, total_distance, max_edge_distance

# Perform the heuristic search
tour, total_cost, max_distance = find_bottleneck_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)