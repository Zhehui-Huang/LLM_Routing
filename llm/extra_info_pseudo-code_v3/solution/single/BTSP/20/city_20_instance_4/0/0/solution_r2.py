import math

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

# Generate all possible edges with distances
edges = [(i, j, calculate_distance(i, j)) for i in cities for j in cities if i != j]
edges.sort(key=lambda x: x[2])

# Critical part: trying to find a Hamiltonian cycle with minimized maximum edge length
def find_minimized_max_edge_cycle():
    for dist in sorted(set(edge[2] for edge in edges)):
        edges_up_to_dist = [e for e in edges if e[2] <= dist]
        
        # Represent graph with adjacency list
        graph = {i: [] for i in cities}
        for u, v, _ in edges_up_to_dist:
            graph[u].append(v)
            graph[v].append(u)
        
        # DFS attempt to find a valid tour
        all_visited = set()
        def dfs(city, path):
            if len(path) == len(cities):
                if path[0] in graph[city]:  # Check cycle condition
                    return path + [path[0]]
                return None
            
            for neighbor in graph[city]:
                if neighbor not in path:
                    result = dfs(neighbor, path + [neighbor])
                    if result is not None:
                        return result
            return None
        
        # Try to start DFS from any city as the starting point
        tour = dfs(0, [0])
        if tour:
            # Calculate the metrics required
            max_edge_length = max(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            total_travel_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            return tour, total_travel_cost, max_edge_length

# Call the function to compute the tour
tour_result = find_minimized_max_edge_cycle()
if tour_result:
    tour, total_cost, max_gap = tour_result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_gap)
else:
    print("A feasible solution could not be found.")