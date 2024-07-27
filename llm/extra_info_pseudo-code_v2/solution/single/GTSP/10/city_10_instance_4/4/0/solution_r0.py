import numpy as np
import itertools

# Define cities and their coordinates
cities = {
    0: (79, 15),  # depot
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# City groups
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours by taking one city from each group and returning to the depot
def all_possible_tours(groups, depot):
    for group_combination in itertools.product(*groups):
        yield [depot, *group_combination, depot]

# Evaluate the cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Finding the shortest tour
def find_shortest_tour(groups, depot):
    best_tour = None
    min_cost = float('inf')
    for tour in all_possible_tours(groups, depot):
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Execution of the tour finding function
best_tour, total_cost = find_shortest_tour(groups, 0)

# Outputting the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")