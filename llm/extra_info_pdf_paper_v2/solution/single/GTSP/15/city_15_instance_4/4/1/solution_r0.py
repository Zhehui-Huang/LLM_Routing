import itertools
import math

# Environment setup: coordinates of all cities including the depot
cities = [
    (35, 40),  # Depot City 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Group of cities
city_groups = [
    [3, 8],    # Group 0
    [4, 13],   # Group 1
    [1, 2],    # Group 2
    [6, 14],   # Group 3
    [5, 9],    # Group 4
    [7, 12],   # Group 5
    [10, 11]   # Group 6
]

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all possible combinations, each combination includes exactly one city from each group
all_combinations = list(itertools.product(*city_groups))

# Function to calculate the tour cost
def calculate_tour_cost(tour):
    total_cost = euclidean_distance(0, tour[0])  # Start from depot
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    total_cost += euclidean_distance(tour[-1], 0)  # Return to depot
    return total_cost

# Finding the shortest tour
shortest_tour = None
min_cost = float('inf')

for combination in all_combinations:
    cost = calculate_tour_cost(combination)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = combination

# Formatting the output
if shortest_tour is not None:
    result_tour = [0] + list(shortest_tour) + [0]
    print(f'Tour: {result_tour}')
    print(f'Total travel cost: {min_cost:.2f}')
else:
n    print("No viable tour found.")