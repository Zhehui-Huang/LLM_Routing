from itertools import combinations
from math import sqrt
import sys

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 38),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Euclidean distance calculation
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 7 cities excluding the depot
combs = combinations([i for i in range(1, 15)], 7)

best_tour = None
best_cost = sys.float_info.max

# Check all combinations
for comb in combs:
    cities_in_tour = [0] + list(comb) + [0]  # Create tour starting and ending at depot
    # Find the shortest path using a greedy algorithm
    for start in range(1, 8):  # Try different starting points for the permutation
        current_tour = cities_in_tour[:1] + cities_in_tour[start:start+1] + cities_in_tour[1:start] + cities_in_tour[start+1:]
        current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost

# Construct the tour and calculate the cost
final_tour = best_tour
final_cost = sum(distance(final_tour[i], final_tour[i+1]) for i in range(len(final_tour)-1))

# Output the result
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")