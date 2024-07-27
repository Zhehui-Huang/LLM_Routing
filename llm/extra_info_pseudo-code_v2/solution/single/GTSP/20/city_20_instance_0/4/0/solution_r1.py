import math
import itertools

# Define the cities and their positions
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Define the groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def euclidean_distance(city1, city2):
    """ Compute the Euclidean distance between two cities, identified by their indices. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour):
    """ Calculate the total distance of the tour. """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])  # Correct function call
    return total_distance

def find_best_tour():
    """ Find the best tour starting and ending at the depot, visiting one city from each group. """
    min_cost = float('inf')
    best_tour = None

    # Iterate over all combinations, one from each group
    for combo in itertools.product(*groups):
        all_possibilities = list(itertools.permutations(combo))
        depot = 0

        for possibility in all_possibilities:
            tour = [depot] + list(possibility) + [depot]
            cost = calculate_total_distance(tour)

            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Run the function to find the best tour
best_tour, min_cost = find_best_tour()

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")