from itertools import permutations
import math

# Given city coordinates and groups
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Find the shortest tour solving the GTSP variant
def find_shortest_tour(groups):
    smallest_distance = float('inf')
    best_tour = None

    # Generate all combinations each taking one city from each group  
    for group_selection in permutations([min(group, key=lambda x: distance(0, x)) for group in groups.values()]):
        # Construct permutations including starting and ending at the depot
        all_tours = permutations(group_selection)
        for tour in all_tours:
            tour = [0] + list(tour) + [0]
            total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if total_cost < smallest_distance:
                smallest_distance = total_cost
                best_tour = tour

    return best_tour, smallest_distance

# Execute the calculation
tour, total_cost = find_shortest_tour(groups)

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")