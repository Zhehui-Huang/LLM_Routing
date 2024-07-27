import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate all possible tours excluding the depot city initially and then adding it at start and end
all_tours = permutations([i for i in cities if i != 0])
best_tour = None
min_cost = float('inf')

for tour in all_tours:
    current_tour = [0] + list(tour) + [0]
    current_cost = get_total_distance(current_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output the best tour and the minimum cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))