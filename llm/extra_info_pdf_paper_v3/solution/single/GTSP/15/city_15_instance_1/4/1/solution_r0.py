import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of city groups with one city taken from each group
def generate_all_possible_tours():
    for representative_set in permutations([min(group, key=lambda x: distance(0, x)) for group in groups]):
        yield [0] + list(representative_set) + [0]

# Function to calculate total tour cost
def total_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Find the optimal tour from all possible tours
best_tour = None
best_cost = float('inf')

for possible_tour in generate_all_possible_tours():
    cost = total_tour_cost(possible_tour)
    if cost < best_cost:
        best_tour = possible_tour
        best_cost = cost

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")