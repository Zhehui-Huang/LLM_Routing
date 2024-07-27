import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Generate all possible representative permutations
group_permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
best_tour = None
best_cost = float('inf')

for perm in group_permutations:
    # For each permutation of the groups, try picking one city from each group in this order
    for city_combo in itertools.product(*[groups[i] for i in perm]):
        current_tour = [0] + list(city_combo) + [0]
        current_cost = calculate_total_cost(current_tour, coordinates)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
            
# Ensure to print the results
print("Tour:", best_tour)
print("Total travel import itertoolscost:", best_cost)