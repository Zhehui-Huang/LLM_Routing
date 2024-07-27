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

# Generate all possible tours by selecting one city from each group
all_possible_tours = permutations([g[0] for g in groups], len(groups))

# Loop to find the minimum cost tour
min_cost = float('inf')
min_tour = None

for perm in all_possible_tours:
    current_tour = [0]  # start at the depot
    current_tour.extend(perm)
    current_tour.append(0)  # return to the depot

    # Calculate the total cost of this tour
    total_cost = 0
    for i in range(len(current_tour) - 1):
        total_cost += distance(current_tour[i], current_tour[i + 1])

    # Update the minimum cost
    if total_ cost < min_cost:
        min_cost = total_cost
        min_tour = current_tour

# Output the results
print("Tour:", min_tour)
print("Total travel cost:", round(min_cost, 2))