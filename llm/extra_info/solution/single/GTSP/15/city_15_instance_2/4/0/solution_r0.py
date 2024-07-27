import itertools
import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
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

city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean distance(i, j)

# Initialize minimum tour cost high and selected tour empty
min_cost = float('inf')
selected_tour = []

# Iterating over each combination of one city from each group
for comb in itertools.product(*city_groups):
    # Start & end at depot, include the combination of chosen cities
    tour = [0] + list(comb) + [0]
    # Calculate the total cost of this tour
    cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    # Update minimum cost and tour if found better
    if cost < min_cost:
        min_cost = cost
        selected_tour = tour

# Output the selected tour and cost
print(f"Tour: {selected_tour}")
print(f"Total travel cost: {min_cost}")