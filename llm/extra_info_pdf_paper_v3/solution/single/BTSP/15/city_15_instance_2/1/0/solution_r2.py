import math
from itertools import permutations

# Define city coordinates
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

# Euclidean distance function between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate the tour problem
def find_best_tour():
    min_max_distance = float('inf')
    best_tour = None
    total_cost = 0

    for perm in permutations(range(1, len(cities))):
        # Add the depot city at the beginning and the end
        route = [0] + list(perm) + [0]

        # Calculate the cost and max distance
        current_max_distance = 0
        current_total_cost = 0
        for i in range(len(route) - 1):
            distance = euclidean_distance(route[i], route[i + 1])
            current_total_cost += distance
            if distance > current_max_distance:
                current_max_distance = distance
        
        # Update the best found tour
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            best_tour = route
            total_cost = current_total_cvost

    return best_tour, total_cost, min_max_distance

# Solve the problem
best_tour, total_cost, max_distance = find_best_tour()

# Print results
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))