import itertools
import math

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance between two points
def euc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euc_dist(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate all possible tours where exactly one city from each group is visited
def find_best_tour():
    best_tour = None
    min_cost = float('inf')
    
    # Generate all combinations of cities picking one from each group
    for combination in itertools.product(*groups):
        current_tour = [0] + list(combination) + [0]  # Starting and ending at the depot
        current_cost = tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
            
    return best_tour, min_cost

# Find the best tour
best_tour, min_cost = find_best_tour()

# Output format
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")