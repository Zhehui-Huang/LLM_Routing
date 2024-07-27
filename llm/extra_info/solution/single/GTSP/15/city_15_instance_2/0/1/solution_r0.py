from itertools import product
import math

# Coordinates of all cities including the depot
city_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Grouping of the cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    total_cost = euclidean_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    total_cost += euclidean_distance(tour[-1], 0)  # Return to depot
    return total_cost

# Generate all combinations of cities, taking one from each group
all_combinations = product(*groups)

best_tour = None
best_cost = float('inf')

for combination in all_combinations:
    tour = [0] + list(combination) + [0]
    cost = calculate_tour_cost(list(combination))
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)