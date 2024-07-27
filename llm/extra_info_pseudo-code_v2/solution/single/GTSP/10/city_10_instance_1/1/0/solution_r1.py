import itertools
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates
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

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Generate all combinations of one city from each group
# We use itertools.product to get Cartesian product of lists from groups
all_combinations = list(itertools.product(*groups))

# Helper function to compute the total distance of a tour
def compute_tour_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    # Close the tour by returning to the starting point
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_distance

# Calculate shortest tour from all possible tours
best_tour = None
min_distance = float('inf')

for combination in all_combinations:
    current_tour = [0] + list(combination) + [0]
    current_distance = compute_tour_distance(current_tour, cities)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")