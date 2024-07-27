from math import sqrt
from itertools import combinations

# Coordinates for the cities
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

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Held-Karp dynamic programming approach
def held_karp():
    # Distance dictionary for all city pairs
    dist = {(i, j): distance(i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j}

    # Cost dictionary
    C = {}
    
    # Base cases
    for k in range(1, len(cities)):
        C[(1 << k, k)] = (dist[0, k], 0)

    # Dynamic programming to compute the shortest tour
    for subset_size in range(2, len(cities)):
        for subset in combinations(range(1, len(cities)), subset_size):
            bits = sum(1 << b for b in subset)
            for k in subset:
                prev = bits & ~(1 << k)
                C[(bits, k)] = min((C[(prev, m)][0] + dist[m, k], m) for m in subset if m != k)
                
    # Closure to forming a complete tour returning to the starting city
    all_visited = (1 << len(cities)) - 1
    min_cost, last_city = min((C[(all_visited & ~(1 << 0), k)][0] + dist[k, 0], k) for k in range(1, len(cities)))

    # Reconstructing the path based on the minimum cost data collected
    path = [0]
    for i in range(len(cities) - 1):
        path.append(last_city)
        next_last_city = C[(all_visited, last_city)][1]
        all_visited &= ~(1 << last_city)
        last_city = next_last_city

    # Complete the tour by going back to the starting city
    path.append(0)
    return path, min_cost

# Execute the algorithm
tour_path, tour_cost = held_karp()

# Print the results
print("Tour:", tour_path)
print("Total travel cost:", tour_cost)