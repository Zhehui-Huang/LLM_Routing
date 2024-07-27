import math
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    dx = cities[city1][0] - cities[city2][0]
    dy = cities[city1][1] - cities[city2][1]
    return math.sqrt(dx**2 + dy**2)

# Precompute distances between all pairs of cities
dist = {}
for i in cities:
    for j in cities:
        if i != j:
            dist[(i, j)] = distance(i, j)

### Step 2: Implement the Held-Karp algorithm

def held_karp():
    # Base case
    C = {(frozenset([0, i]), i): (dist[0, i], [0, i]) for i in cities if i != 0}
    
    # Recursive step
    for s in range(2, len(cities)):
        for S in [frozenset([0] + list(comb)) for comb in combinations(cities, s) if 0 in comb]:
            for j in S - {0}:
                C[(S, j)] = min([(C[(S - {j}, k)][0] + dist[k, j], C[(S - {j}, k)][1] + [j]) for k in S if k != j and k != 0], key=lambda x: x[0])
    
    # Closing the tour
    all_cities = frozenset(cities)
    result = min([(C[(all_cities, j)][0] + dist[j, 0], C[(all_cities, j)][1] + [0]) for j in cities if j != 0], key=lambda x: x[0])
    
    return result

### Compute the result

result = held_karp()
tour, total_cost = result[1], result[0]

### Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")