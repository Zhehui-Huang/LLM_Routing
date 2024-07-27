import math
from itertools import permutations

# Coordinates of cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create list of all possible edges with their distances
edges = [(i, j, euclidean_distance(i, j)) for i in range(10) for j in range(10) if i != j]
edges = sorted(edges, key=lambda x: x[2])  # Sort by distance

def is_hamiltonian_path(vertices, threshold):
    """ Check whether there is a Hamiltonian path in the graph under the given threshold. """
    # Generate all permutations of the cities (except the starting depot 0)
    for perm in permutations(vertices):
        if perm[0] == 0:  # ensure it starts with depot
            valid = True
            max_edge = 0
            for i in range(len(perm) - 1):
                dist = euclidean_distance(perm[i], perm[i + 1])
                if dist > threshold:
                    valid = False
                    break
                max_edge = max(max_edge, dist)
            if valid:
                return True, perm, max_edge
    return False, [], 0

def btsp():
    """ Main function to solve the Bottleneck Traveling Salesman Problem. """
    for weight in edges:  # iterate over each edge sorted by weight
        threshold = weight[2]
        has_path, path, max_edge = is_hamiltonian_path(range(10), threshold)
        if has_path:
            # Calculate the total distance of the path
            total_distance = sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))
            # Ensure the path returns to the depot
            total_distance += euclidean_distance(path[-1], path[0])
            max_edge = max(max_edge, euclidean64_distance(path[-1], path[0]))
            path += (path[0],)
            return f"Tour: {list(path)}\nTotal travel cost: {total_distance}\nMaximum distance between consecutive cities: {max_edge}"
    return "No solution found."

# Execute the BTSP function
print(btsp())