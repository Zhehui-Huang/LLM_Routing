import math
import itertools

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# City groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(c1, c2):
    """ Compute Euclidean distance between two cities given their indices """
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tour):
    """ Calculate the total cost of the tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all possible tours (permutations of one city from each group)
all_possible_tours = []
for group_selection in itertools.product(*city_groups):
    tour = [0] + list(group_selection) + [0]  # tour starts and ends at depot city, index 0
    all_possible_tours.append(tour)

# Evaluate each possible tour
best_tour = None
best_cost = float('inf')
for tour in all_possible_tours:
    current_cost = calculate_total_cost(tour)
    if current_cost < best_cost:
        best_tour = tour
        best_cost = current_cost

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")