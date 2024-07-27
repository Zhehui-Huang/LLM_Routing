import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates indexed from 0 to 19
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Given solution to be tested
edges = [
    (0, 3), (2, 13), (6, 13), (15, 17), (3, 19), (5, 15),
    (6, 19), (5, 17), (2, 6), (9, 16), (3, 15), (0, 15),
    (1, 10), (7, 18), (5, 19), (3, 5), (0, 19), (4, 7),
    (12, 18), (7, 12), (1, 4), (8, 14), (13, 19), (0, 5),
    (7, 14), (4, 18), (15, 19), (3, 6), (10, 11), (5, 6),
    (0, 1), (3, 17), (0, 17), (2, 19), (16, 17)
]

def verify_solution(cities, edges):
    # Check each city is visited exactly once
    visited = set()
    for edge in edges:
        visited.add(edge[0])
        visited.add(edge[1])

    if len(visited) != len(cities):
        return "FAIL"
    
    # Find a continuous tour from the edges and calculate costs
    from collections import defaultdict
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    # Attempt to find a Eulerian path (each vertex has even degree except start and end)
    odd_degree_vertices = [k for k, v in graph.items() if len(v) % 2 != 0]
    if len(odd_degree_vertices) != 2 and len(odd_degree_vertices) != 0:
        return "FAIL"
    if 0 not in odd_degree_vertices:
        return "FAIL"

    # Find path starting from depot city (0) - using DFS to simulate finding Eulerian path
    start_node = 0
    stack = [start_node]
    path = []
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
            # Remove the edge in both directions
            graph[next_node].remove(node)
        else:
            path.append(stack.pop())

    if path[0] != 0 or path[-1] != 0:
        return "FAIL"

    # Check total cost and the maximum distance between consecutive cities
    total_cost = 0
    maximum_distance = 0
    for i in range(len(path) - 1):
        distance = calculate_distance(cities[path[i]], cities[path[i + 1]])
        total_cost += distance
        maximum_distance = max(maximum_distance, distance)

    if maximum_distance != 30.4138126514911:
        return "FAIL"

    return "CORRECT"

# Running the test
test_result = verify_solution(cities, edges)
print(test_result)