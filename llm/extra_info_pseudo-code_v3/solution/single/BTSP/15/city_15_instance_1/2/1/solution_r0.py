import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_hamiltonian_path(graph, start_node):
    visited = set()
    def visit(vertex, count):
        visited.add(vertex)
        if len(visited) == len(graph):
            return True
        for neighbor in graph[vertex]:
            if neighbor not in visited and visit(neighbor, count+1):
                return True
        visited.remove(vertex)
        return False
    return visit(start_node, 1)

def construct_bottleneck_graph(cities, max_distance):
    graph = {i: [] for i in range(len(cities))}
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            if calculate_distance(cities[i], cities[j]) <= max_distance:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def solve_btsp(cities):
    edges = [
        (calculate_distance(cities[i], cities[j]), i, j)
        for i in range(len(cities)) for j in range(i+1, len(cities))
    ]
    edges.sort()
    
    for max_distance, _, _ in edges:
        graph = construct_bottleneck_graph(cities, max_distance)
        if check_hamiltonian_path(graph, 0):
            path = [0]
            visited = set([0])
            current = 0
            while len(path) < len(cities):
                next_city = min((city for city in graph[current] if city not in visited), key=lambda x: calculate_distance(cities[current], cities[x]))
                path.append(next_city)
                visited.add(next_city)
                current = next_city
            path.append(0)  # Return to the depot
            total_cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            max_leg_distance = max(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            return path, total_cost, max_leg_distance
    return None

# Cities coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

path, total_cost, max_leg_distance = solve_btsp(cities)

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)