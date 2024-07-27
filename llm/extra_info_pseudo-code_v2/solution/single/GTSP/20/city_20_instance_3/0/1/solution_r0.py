import math
import itertools

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible city selections (one from each group)
all_possible_selections = itertools.product(*groups)

# Evaluate each selection by creating a full tour and calculating its cost
best_tour = None
best_cost = float('inf')

for selection in all_possible_selections:
    # We always start at the depot, and end at the depot
    possible_tours = itertools.permutations(selection)
    for tour in possible_tours:
        tour = [0] + list(tour) + [0]   # Adding the depot as the start and end
        cost = total_tour_cost(tour)
        if cost < best_cost:
            best_tour, best_cost = tour, cost

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))