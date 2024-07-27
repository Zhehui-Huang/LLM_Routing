import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define city groups
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return cost

# Generating all possible combinations of tours
# where exactly one city from each group is visited
best_tour = None
min_cost = float('inf')

# Iterate over all permutations of one city from each group
for group_0 in groups[0]:
    for group_1 in groups[1]:
        for group_2 in groups[2]:
            for group_3 in groups[3]:
                current_tour = [0, group_0, group_1, group_2, group_3, 0]  # depot -> cities -> depot
                current_cost = calculate_tour_cost(current_tour)
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_tour = current_tour

# Output the best tour and its cost
print("Tour: " + str(best_tour))
print("Total travel cost:", min_cost)