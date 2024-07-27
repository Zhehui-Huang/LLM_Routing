import itertools
import math

# Define the positions of cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define the city groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate all possible representative city selections (one per group)
representative_permutations = list(itertools.product(*city_groups))

# Find the shortest tour
min_cost = float('inf')
best_tour = None

for permutation in representative_permutations:
    # Consider all permutations of the selected representatives
    for perm in itertools.permutations(permutation):
        current_cost = distance(0, perm[0])
        # Create the tour starting with the depot
        current_tour = [0] + list(perm) + [0]
        # Calculate the total travel cost
        for i in range(len(perm) - 1):
            current_cost += distance(perm[i], perm[i + 1])
        current_cost += distance(perm[-1], 0)
        # Update the minimum cost and best tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the best tour and the corresponding cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))