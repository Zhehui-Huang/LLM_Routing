import math
from itertools import product

# Coordinates of the depot and cities
locations = [
    (3, 26),   # Depot 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48),  # City 19
]

# Groups of city indices
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate all-pairs Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((locations[i][0] - locations[j][0])**2 + (locations[i][1] - locations[j][1])**2)

N = len(locations)
dist = [[euclidean_dist(i, j) for j in range(N)] for i in range(N)]


# Function to solve the modified TSP
def solve_tsp_dp(groups, dist):
    all_cities = [0] + [min(group) for group in groups]  # Starting with the depot and the first city in each group
    set_size = len(all_cities)
    DP = {}
    
    # Initialize
    for i in range(1, set_size):
        DP[(1 << i, i)] = (dist[0][all_cities[i]], [0, all_cities[i]])
    
    # Subset DP
    for s in range(2, set_size):
        for S in (set for set in product([0, 1], repeat=set_size) if sum(set) == s and set[0] == 1):
            S_bits = sum(1 << i for i, bit in enumerate(S) if bit)
            for j in range(1, set_size):
                if not S[j]:
                    continue
                prev_state = S_bits & ~(1 << j)
                candidate_paths = []
                for k in range(1, set_size):
                    if not S[k]:
                        continue
                    previous_cost, previous_tour = DP[(prev_state, k)]
                    candidate_paths.append((previous_cost + dist[all_cities[k]][all_cities[j]], previous_tour + [all_cities[j]]))
                DP[(S_bits, j)] = min(candidate_paths)
                
    # Construct the answer
    final_candidates = [(DP[(2**set_size - 1, j)][0] + dist[all_cities[j]][0], DP[(2**set_size - 1, j)][1] + [0]) for j in range(1, set_size)]
    min_cost, min_tour = min(final_candidates)
    return min_tour, min_cost

# Solve the TSP
selected_cities = [min(group, key=lambda x: dist[0][x]) for group in groups]
optimal_tour, total_cost = solve_tsp_dp(groups, dist)

print("Tour:", optimal_tour)
print("Total travel cost: {:.2f}".format(total_cost))