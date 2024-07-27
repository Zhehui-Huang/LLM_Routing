from itertools import permutations
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate all pairwise distances (complete graph)
distances = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to determine if a Hamiltonian circuit exists from a sorted list of edges, within a given max distance
def find_hamiltonian_circuit(max_dist):
    num_cities = len(cities)
    adjacency_list = [[] for _ in range(num_cities)]
    
    # Construct the bottleneck graph with the maximum allowed edge distance
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if distances[i][j] <= max_dist:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)
    
    # Test all permutations for a valid tour; this brute force method is feasible for small problem sizes
    for permutation in permutations(range(1, num_cities)):  # Keep 0 (depot) as the start and end point
        valid = True
        prev = 0
        max_edge = 0
        for node in permutation:
            if node not in adjacency_list[prev]:
                valid = False
                break
            max_edge = max(max_edge, distances[prev][node])
            prev = node
        if valid and 0 in adjacency
        adjacency_list[node]:  # Check return to depot condition
            cycle = [0] + list(permutation) + [0]
            max_edge = max(max_edge, distances[node][0])
            return (True, cycle, max_edge)
    return (False, None, None)

# Search for the minimal bottleneck value that has a valid Hamiltonian cycle
sorted_distances = sorted(list(set(distances[i][j] for i in range(num_cities) for j in range(i + 1, num_cities))))
lo, hi = 0, len(sorted_distances) - 1
best_tour = None
while lo <= hi:
    mid = (lo + hi) // 2
    has_path, tour, max_edge = find_hamiltonian_circuit(sorted_distances[mid])
    if has_path:
        best_tour = (tour, max_edge, sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1)))
        hi = mid - 1
    else:
        lo = mid + 1

if best_tour:
    print(f"Tour: {best_tour[0]}")
    print(f"Total travel cost: {best_tour[2]}")
    print(f"Maximum distance between consecutive cities: {best_tour[1]}")
else:
    print("No solution found.")