import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of cities selecting one from each group
all_possible_selections = list(permutations([c for group in groups for c in group], len(groups)))

# Generate valid tours from the combinations
valid_tours = []
for selection in all_possible_selections:
    if all(any(city in group for city in selection) for group in groups):
        valid_tours.append(selection)

# Find the shortest valid tour
min_cost = float('inf')
min_tour = None

for tour in valid_tours:
    # Add the depot at the start and end of the tour
    tour_with_depot = [0] + list(tour) + [0]

    # Calculate the total cost of this tour
    total_cost = sum(distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot)-1))

    # Update the minimum cost and tour if a new minimum is found
    if total_cost < min_cost:
        min_cost = total_cost
        min_tour = tour_with_deft_ot

# Output the results
print("Tour:", min_tour)
print("Total travel cost:", round(min_cost, 2))