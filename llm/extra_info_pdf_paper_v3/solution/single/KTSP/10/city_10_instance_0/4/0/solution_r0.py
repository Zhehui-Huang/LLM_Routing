from itertools import combinations, permutations
import math

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Finding all combinations of 3 cities, excluding depot city 0 (which must be in the tour)
combinations_of_cities = combinations([i for i in range(1, 10)], 3)

# The shortest path and its cost initialization
shortest_path = []
min_cost = float('inf')

for combination in combinations_of_cities:
    current_combination = (0,) + combination + (0,)  # Adding depot city to the current set
    for perm in permutations(current_combination):
        if perm[0] == 0 and perm[-1] == 0:  # ensure that we start and end at the depot
            current_cost = sum(euclidean_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_path = list(perm)

# Output Result
print(f"Tour: {shortest_path}")
print(f"Total travel cost: {min_cost:.2f}")