import math
import itertools

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_tour_cost(tour, cities):
    """Calculate the total travel cost of a tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# City groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Generate all possible combinations of cities, one from each group
def generate_all_combinations(groups):
    return list(itertools.product(*groups))

all_combinations = generate_all_combinations(groups)

# Find the optimal tour
best_tour = None
best_cost = float('inf')

for combination in all_combinations:
    raw_tour = [0] + list(combination) + [0]
    cost = calculate_tour_cost(raw_tour, cities)
    if cost < best_cost:
        best_tour = raw_tour
        best_cost = cost

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")