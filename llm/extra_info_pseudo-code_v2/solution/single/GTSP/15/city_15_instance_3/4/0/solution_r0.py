import math
import itertools

# Define the coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define the groups of cities
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations, one city from each group
possible_tours = list(itertools.product(*groups))

# Function to compute total travel cost for a given tour
def total_cost(tour):
    total = distance(0, tour[0]) + distance(tour[-1], 0)
    for i in range(len(tour) - 1):
        total += distance(tour[i], tour[i + 1])
    return total

# Find the shortest tour
shortest_tour = None
min_cost = float('inf')
for tour in possible_tours:
    cost = total_cost(tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour

# Convert to expected output format
result_tour = [0] + list(shortest_tour) + [0]

# Print the output
print("Tour:", result_tour)
print("Total travel cost:", min_cost)