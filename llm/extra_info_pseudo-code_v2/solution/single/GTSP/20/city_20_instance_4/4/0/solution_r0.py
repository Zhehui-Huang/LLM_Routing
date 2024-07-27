import itertools
import math

# Given city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
groups = {
    0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 3: [1, 3, 9],
    4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
}

# Calculate Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of cities selecting one from each group
possible_tours = itertools.product(*groups.values())

# Find the shortest path from these combinations
best_tour = None
min_cost = float('inf')

for tour in possible_tours:
    # Loop over each combination, adding the depot at the start and end
    full_tour = [0] + list(tour) + [0]
    # Calculate the cost of this tour
    total_cost = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
    # Update best tour if this one is better
    if total_cost < min_cost:
        best_tour = full_tour
        min_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")