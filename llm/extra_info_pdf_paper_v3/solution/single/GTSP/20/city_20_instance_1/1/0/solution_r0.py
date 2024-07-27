import itertools
import math

# Given cities and coordinates
cities = {
    0: (14, 77),  # depot
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Grouping of cities
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of one city from each group
group_city_permutations = list(itertools.product(groups[0], groups[1], groups[2], groups[3]))

# Find best tour starting and ending at the depot city 0
min_tour_cost = float('inf')
best_tour = []

for perm in group_city_permutations:
    # Consider all permutations of the cities in the combination to account for different visiting orders
    for city_seq in itertools.permutations(perm):
        # Calculate the tour cost from the depot, through the sequence, and back to the depot
        tour_cost = distance(0, city_seq[0])  # from depot to first city
        for i in range(len(city_seq) - 1):
            tour_cost += distance(city_seq[i], city_seq[i + 1])
        tour_cost += distance(city_seq[-1], 0)  # from last city back to depot

        # Update the best tour found so far
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = [0] + list(city_seq) + [0]

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_tour_cost:.2f}")