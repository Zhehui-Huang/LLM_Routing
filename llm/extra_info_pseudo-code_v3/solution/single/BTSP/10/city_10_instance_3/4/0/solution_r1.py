import math
from itertools import permutations

# Coordinates of cities defined as before
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

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all edges with distances
edges = [(i, j, euclidean_distance(i, j)) for i in range(10) for j in range(i+1, 10)]
edges.sort(key=lambda x: x[2])  # Sort edges by distance

def find_hamiltonian_cycle(threshold):
    """ Check if there is a Hamiltonian cycle below the given threshold weight.
    """
    # Create graph with edges having weight less than or equal to threshold
    graph = [set() for _ in range(10)]
    for i, j, weight in edges:
        if weight <= threshold:
            graph[i].add(j)
            graph[j].add(i)
    
    # Try to form a Hamiltonian cycle starting and ending at 0
    for perm in permutations(range(1, 10)):  # generate permutations of nodes except 0
        if all(perm[i] in graph[perm[i-1]] for i in range(1, 9)) and perm[-1] in graph[perm[0]] and perm[0] in graph[0] and perm[-1] in graph[0]:
            # Check if complete path meets threshold
            total_distance = 0
            max_edge = 0
            path = (0,) + perm + (0,)
            for i in range(10):
                dist = euclidean_distance(path[i], path[i+1])
                if dist > max_edge:
                    max_edge = dist
                total_distance += dist
            return True, path, total_distance, max_edge
    return False, [], 0, 0

def btsp():
    """ Solve the Bottleneck TSP, attempting to minimize maximum edge weight in tour. """
    l, r = 0, max(edge[2] for edge in edges)  # Binary search bounds
    best_tour, best_total, best_max_distance = [], float('inf'), float('inf')
    
    while l <= r:
        mid = (l + r) / 2
        found, tour, total_distance, max_distance = find_hamiltonian_cycle(mid)
        if found:
            if total_distance < best_total:
                best_tour, best_total, best_max_distance = tour, total_distance, max_distance
            r = mid - 1
        else:
            l = mid + 1
    
    if best_tour:
        return f"Tour: {best_tour}\nTotal travel cost: {best_total}\nMaximum distance between consecutive cities: {best_max_distance}"
    else:
        return "No valid tour found."

# Execute the BTSP function to find the optimal tour
print(btsp())