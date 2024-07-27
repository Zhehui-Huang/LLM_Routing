from itertools import combinations
from math import sqrt

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Build distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

def held_karp():
    # C stores the cost of reaching each subset of the nodes ending in node k
    C = {}

    # Base case: just to start from the depot
    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], [0, k])

    # Iterate over all subsets of the cities
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            # Set bits for all cities in the subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the cost of the cheapest path through all the subset's cities
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k: continue
                    if (prev, m) in C:
                        curr_cost = C[(prev, m)][0] + distances[m][k]
                        if (bits, k) not in C or curr_cost < C[(bits, k)][0]:
                            C[(bits, k)] = (curr_cost, C[(prev, m)][1] + [k])

    # Return to depot from each node in the set all nodes
    bits = (2**n - 1) - 1
    min_cost, path = min((C[(bits, k)][0] + distances[k][0], C[(bits, k)][1] + [0]) for k in range(1, n))

    return min_cost, path

# Get the optimal tour and its cost
min_cost, path = held_karp()

# Print results
print("Tour:", path)
print("Total travel cost:", min_cost)