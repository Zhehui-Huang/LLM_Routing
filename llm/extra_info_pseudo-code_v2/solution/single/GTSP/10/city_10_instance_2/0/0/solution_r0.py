import random
import math
import itertools

# Define the coordinates of each city
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define the groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations for choosing one city from each group
all_combinations = list(itertools.product(*groups))

# Function to evaluate the total path cost of visiting the cities in order
def evaluate_tour(tour):
    total_dist = distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i + 1])
    total_dist += distance(tour[-1], 0)  # from last city back to depot
    return total_dist

# Find tour with the minimum travel cost
min_cost = float('inf')
best_tour = None

for combination in all_combbinations:
    cost = evaluate_tour(combination)
    if cost < min_cost:
        min_cost = cost
        best_tour = combination

# Convert the best tour into the required output format
final_tour = [0] + list(best_tour) + [0]

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {min_cost:.2f}")