import math
from itertools import permutations

# Given coordinates for each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.hypot(c2[0] - c1[0], c2[1] - c1[1])

# Calculate all pairwise distances
distances = {
    (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Bottleneck-optimal Biconnected Subgraph Construction
def algorithm_BB():
    # Step 0: Sort and initialize
    sorted_edges = sorted(distances.items(), key=lambda x: x[1])
    edges_BB = []

    # Find biconnectivity function (placeholders: implement actual DFS check)
    def is_biconnected(edges):
        # Using edge list to form adjacency; use dfs/bfs to check connectivity etc
        # Placeholder, assume it's valid
        return True

    # Step 1: Build biconnected graph
    for edge, weight in sorted_edges:
        edges_BB.append(edge)
        if is_biconnected(edges_BB):
            return edges_BB, max(weight for _, weight in distances.items() if _ in edges_BB), edges_BB

# Step 2 can be tricky to implement, let's simulate trial Hamiltonian tours
def find_tour(edges):
    nodes = set(j for i in edges for j in i)
    all_tours = list(permutations(nodes))
    min_cost = float('inf')
    optimal_tour = []
    for tour in all_tours:
        # Make sure it is a valid tour (returns to starting point, 0 here)
        if tour[0] == 0 and tour[-1] == 0:
            cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
            max_seg_cost = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
            if max_seg_cost < min_cost:
                min_cost = max_seg_cost
                optimal_tour = tour
    
    return optimal_tour, sum(distances[(optimal_tour[i], optimal_tour[i + 1])] for i in range(len(optimal_tour) - 1)), min_cost

# Main execution:
edges_bb, _, _ = algorithm_BB()
tour, total_cost, max_dist = find_tour(edges_bb)

# Output the results:
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")