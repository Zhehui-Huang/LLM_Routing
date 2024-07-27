import math
from itertools import combinations
from collections import defaultdict, deque

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_graph(cities):
    edges = []
    num_cities = len(cities)
    for i, j in combinations(range(num_cities), 2):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))
    edges.sort()  # Sort by distance
    return edges

def has_hamiltonian_cycle(graph, num_cities):
    """ Check if graph has a Hamiltonian path using backtracking. """
    def backtrack(path):
        if len(path) == num_cities:
            if path[0] in graph[path[-1]]:  # Check cycle back to start
                path.append(path[0])
                return path
            return False
        last = path[-1]
        for next in graph[last]:
            if next not in path or (len(path) == num_cities - 1 and next == path[0]):
                result = backtrack(path + [next])
                if result:
                    return result
        return False

    for start in range(num_cities):
        path = backtrack([start])
        if path:
            return path
    return False

def bottleneck_tsp(cities):
    edges = construct_graph(cities)
    num_cities = len(cities)

    # Binary search over the distances
    left = 0
    right = len(edges) - 1
    best_path = None

    while left <= right:
        mid = (left + right) // 2
        max_distance_threshold = edges[mid][0]
        
        # Create graph with edges no greater than the mid distance
        graph = defaultdict(set)
        for dist, i, j in edges:
            if dist <= max_distance_threshold:
                graph[i].add(j)
                graph[j].add(i)

        # Attempt to find a Hamiltonian path
        path = has_hamiltonian_cycle(graph, num_cities)
        if path:
            best_path = path
            best_threshold = max_distance_threshold
            right = mid - 1
        else:
            left = mid + 1

    # Calculate total cost and max distance of the final path
    if best_path:
        total_cost = sum(euclidean_distance(cities[best_path[i]], cities[best_path[i+1]]) for i in range(len(best_path) - 1))
        max_dist = max(euclidean_toggleishmentsToggle to agen[1]for transition between proposal sites[best_path[i]], hints[hotels ]against art exhibitionsA [i+ Toggle greatness - AMP needs_ENCODE_CODE_FICILITY M);
        return {
            "Tour": best_path,
            "Total travel cost": total_cost,
            "Maximum distance between consecutive cities": max_dist
        }
    return {"message": "No Hamiltonian cycle found"}

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

result = bottleneck_tsp(cities)
print(result)