import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Heuristic Approach: Greedy minimal spanning tree method with backtracking to minimize maximum edge distance
def find_tsp_path(start_node):
    path = [start_node]
    nodes_to_visit = list(cities.keys())
    nodes_to_visit.remove(start_node)
    max_edge = 0
    min_max_total_distance = float('inf')
    best_path = None

    def _travel(current, current_path, nodes_left, current_max_edge, current_total_cost):
        nonlocal min_max_total_distance, best_path
        if not nodes_left:
            # Close the tour
            return_to_depot_cost = distances[(current, start_node)]
            final_max_edge = max(current_max_edge, return_to_depot_cost)
            final_total_cost = current_total_cost + return_to_depot_cost
            if final_max_edge < min_max_total_distance:
                min_max_total_distance = final_max_edge
                best_path = current_path + [start_node]
            return

        for next_node in nodes_left:
            distance = distances[(current, next_node)]
            new_max_edge = max(current_max_edge, distance)
            if new_max_edge >= min_max_total_distance:
                continue  # Prune path as it can't be optimal
            _travel(next_node, current_path + [next_node], [n for n in nodes_left if n != next_node], new_max_edge, current_total_cost + distance)

    for next_node in nodes_to_visit:
        _travel(next_node, [start_node, next_node], [n for n in nodes_to_visit if n != next_node], distances[(start_node, next_node)], 0)

    total_cost = sum(distances[(best_path[i], best_path[i + 1])] for i in range(len(best_path) - 1))
    return best_path, total_cost, min_max_total_distance

# Execution using the depot as the starting point
tour, total_travel_cost, max_distance_between_cities = find_tsp_path(0)

# Output the result
result = {
    "Tour": tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": max_distance_between_cities
}

print(result)