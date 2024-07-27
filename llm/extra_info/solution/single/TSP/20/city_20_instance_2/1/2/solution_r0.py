from math import sqrt
from itertools import combinations

# Defining the cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Held-Karp Algorithm
def held_karp():
    # Distance dictionary
    dist = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}
    
    # Cost dictionary
    C = {}
    
    # Base cases
    for k in range(1, n):
        C[(1 << k, k)] = (dist[0, k], 0)
    
    # Iterate through subsets of increasing length
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            # Find the minimum cost to get to this subset ending at each element k
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k: continue
                    res.append((C[(prev, m)][0] + dist[m, k], m))
                C[(bits, k)] = min(res)
    
    # All city subset
    all_bits = (2 ** n - 1) - 1
    
    # Return the optimal solution
    res = min((C[(all_bits, k)][0] + dist[k, 0], k) for k in range(1, n))
    return res

def calculate_tour():
    # Compute min cost
    min_cost, last_city = held_karp()
    
    # Backtrack to find the path
    tour = [0]
    bits = (2 ** n - 1) - 1
    for i in range(n - 2, -1, -1):
        bits &= ~(1 << last_city)
        _, last_city = C[(bits | (1 << last_city), last_city)]
        tour.append(last_city)
    tour.append(0)
    
    # Correct tour to better format
    tour = list(map(lambda x: x[1:], tour[::-1]))
    return tour, min_cost

# Getting tour and cost
tour, total_cost = calculate_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)