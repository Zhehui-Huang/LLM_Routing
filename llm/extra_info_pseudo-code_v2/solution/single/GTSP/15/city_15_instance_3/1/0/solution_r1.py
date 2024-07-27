import math
import itertools

# Cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# City groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11],
    [2, 8], [3, 9]
]

# Euclidean distance function
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible group combinations for one city per group
group_combinations = list(itertools.product(*groups))

# Function to compute the total cost of a tour
def compute_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour that visits one city from each group and returns to the depot
def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')

    for combination in group_combinations:
        # Consider tours starting at 0, visiting one city from each group, then returning to 0
        tour = [0] + list(combination) + [0]
        cost = compute_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

    return best_tour, best_cost

# Finding the shortest possible tour
optimal_tour, optimal_cost = find_shortest_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)