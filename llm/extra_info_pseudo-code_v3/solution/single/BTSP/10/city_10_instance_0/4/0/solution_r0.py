import math
import itertools

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a complete graph with edge weights
edges = []
for i in range(10):
    for j in range(i+1, 10):
        distance = euclidean_distance(i, j)
        edges.append((distance, i, j))

# Sort edges based on weights
edges.sort()

# Find Bottleneck Hamiltonian Cycle
def find_bottleneck_hamiltonian_cycle():
    for max_weight, u, v in edges:
        # Create bottleneck graph for the current max edge weight
        bottleneck_graph = {i: set() for i in range(10)}
        for weight, i, j in edges:
            if weight <= max_weight:
                bottleneck_graph[i].add(j)
                bottleneck_graph[j].add(i)
        
        # Check if there is a Hamiltonian cycle in the bottleneck graph
        for permutation in itertools.permutations(range(1, 10)):
            valid = True
            max_dist = 0
            prev = 0
            
            # Check if the path is valid in the bottleneck graph
            for node in permutation:
                if node not in bottleneck_graph[prev]:
                    valid = False
                    break
                max_dist = max(max_dist, euclidean_distance(prev, node))
                prev = node

            if valid and 0 in bottleneck_graph[prev]:
                max_dist = max(max_dist, euclidean_distance(prev, 0))
                # Return the valid cycle
                tour = [0] + list(permutation) + [0]
                total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
                return tour, total_cost, max_dist

    return None

# Execute the algorithm to get the results
result = find_bottleneck_hamiltonian_cycle()
if result:
    tour, total_cost, max_distance = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid Hamiltonian cycle found.")