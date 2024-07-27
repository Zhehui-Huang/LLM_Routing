import math
from itertools import combinations

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
n = len(coordinates)


def dist(i, j):
    """Calculate Euclidean distance between cities i and j."""
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 +
                     (coordinates[i][1] - coordinates[j][1]) ** 2)


def held_karp(dists):
    """A Dynamic Programming approach to solve TSP problem."""
    n = len(dists)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2 ** n - 1) - 1
    res = [(C[(bits, k)][0] + dists[k][0], k) for k in range(1, n) if bits & (1 << k)]
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    path.reverse()
    return opt, path


# Compute the distance matrix
distance_matrix = [[dist(i, j) for j in range(n)] for i in range(n)]
optimal_distance, path = held_karp(distance_matrix)

# Calculate cost and format the output
print("Robot 0 Tour:", path)
print("Robot 0 Total Travel Cost:", int(optimal_distance))
print("Overall Total Travel Cost:", int(optimal_distance))