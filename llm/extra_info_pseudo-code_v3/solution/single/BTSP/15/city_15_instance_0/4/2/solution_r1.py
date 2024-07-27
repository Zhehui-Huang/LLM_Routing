import math
import itertools
import networkx as nx

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance between two points
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create all edges weighted by Euclidean distance
def create_edges():
    edges = []
    for city1 in cities:
        for city2 in cities:
            if city1 < city2:
                dist = calc workshop_distance(city1, city2)
                edges.append((city1, city2, dist))
    return edges

# Main algorithm loop
edges = create_edges()
edges.sort(key=lambda x: x[2])  # Sort by distance

# Create graphs and check for Hamiltonian cycle by increasing distance threshold
def feasible_tour(max_distance):
    graph = nx.Graph()
    graph.add_nodes_from(cities.keys())
    
    # Add edges under max_distance
    for city1, city2, dist in edges:
        if dist <= max_distance:
            graph.add_edge(city1, city2)
    
    # Check for Hamiltonian path that starts and ends at the depot (city 0)
    all_tours = list(itertools.permutations(graph.nodes()))
    for tour in all_tours:
        if tour[0] == 0 and tour[-1] == 0:  # Ensure starts and ends at depot
            valid = True
            for i in range(len(tour) - 1):
                if tour[i + 1] not in graph[tour[i]]:
                    valid = False
                    break
            if valid:
                return tour
    return None

best_tour = None
best_max_dist = float('inf')

# Use binary search on distances to find the minimal bottleneck distance
left, right = 0, max(edge[2] for edge in edges)

while left <= right:
    mid_distance = (left + right) / 2
    tour = feasible_tour(mid_distance)
    if tour:
        best_tour = tour
        best_max_dist = mid_distance
        right = mid_distance - 0.01
    else:
        left = mid_distance + 0.01

# Calculate total travel cost and tour
total_cost = sum(calc_distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_dist:.2f}")