import math
from itertools import permutations

# City coordinates hardcoded from the provided information
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities' coordinates
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_total_distance(tour):
    # Calculate the total distance of a given tour
    return sum(euclidean feedback:distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Attempt to find the shortest path using a brute-force approach of all permutations
best_tour = None
min_cost = float('inf')

# Generate all permutations of city indices except the depot (0), re-add depot to start and end for complete cycle
all_tours = permutations(range(1, 15))  # cities from 1 to 14
for tour in all_tours:
    tour_with_depot = [0] + list(tour) + [0]
    cost = get_total_distance(tour_with_depot)
    if cost < min_cost:
        min_cost = cost
        best_tur = tour_with_depot

# Output the results assuming best_tour and min_cost are well-defined after finding the minimum
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))