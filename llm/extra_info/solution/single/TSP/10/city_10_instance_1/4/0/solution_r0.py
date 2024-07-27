from math import sqrt
import itertools

# Coordinates of the cities
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate distances between all pairs
distances = {
    (i, j): distance(i, j) for i in cities for j in cities if i != j
}

# Number of cities including the depot
n = len(cities)

# Held-Karp algorithm for TSP
def held_karp():
    C = {}
    
    # Set distance from depot to depot as 0
    for k in range(1, n):
        C[(1 << k, k)] = (distances[(0, k)], 0)

    # Main loop
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset Smaller subsets
        bits = 0
        for bit in subset:
            bits |= 1 << bit
        
        # Find the shortest path to get to this subset
        for k in subset:
            prev = bits & ~(1 << k)
            res = []
            for m in subset:
                if m == 0 or m == k:
                    continue
                res.append((C[(prev, m)][0] + distances[(m, k)], m))
            C[(bits, k)] = min(res)
    
    # Close the tour
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distances[(k, 0)], k))
    opt, parent = min(res)
    
    # Backtrack to find full path
    tour = [0]
    for i in range(n - 1):
        tour.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    tour.append(0)
    return tour[::-1], opt

# Get optimal tour and the total cost
tour, total_cost = held_karp()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")