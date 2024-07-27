import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def get_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate all possible tours excluding the depot city initially and then adding it as start and end
all_tours = permutations([i for i in cities.keys() if i != 0], len(cities) - 1)
best_tour = None
min_cost = float('inf')

for tour in all_tours:
    # Add the depot city to the start and end of the tour
    current_tour = [0] + list(tour) + [0]
    current_cost = get_total_distance(current_tour)
    # Update the shortest tour found so far
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output the best tour and the minimum cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))