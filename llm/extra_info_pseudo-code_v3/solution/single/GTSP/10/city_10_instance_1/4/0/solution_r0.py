import itertools
import math

# Definitions of cities and their coordinates
cities = {
    0: (53, 68),   # Depot
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

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute all combinations of cities to visit, one from each group
all_combinations = itertools.product(*groups)

# Function to compute the total cost of visiting a list of cities, starting and ending at the depot
def tour_cost(tour):
    total_cost = distance(0, tour[0])  # From depot to first city
    for i in range(1, len(tour)):  # From first city to last city
        total_cost += distance(tour[i - 1], tour[i])
    total_cost += distance(tour[-1], 0)  # From last city back to depot
    return total_cost

# Finding the tour with the minimum distance
min_tour = None
min_cost = float('inf')

for tour in all_combinations:
    current_cost = tour_cost(tour)
    if current_cost < min_cost:
        min_cost = current_cost
        min_tour = tour

# Print the optimal tour starting and ending at the depot city
optimal_tour = [0] + list(min_tour) + [0]
print("Tour:", optimal_tour)
print("Total travel cost:", round(min_cost, 2))