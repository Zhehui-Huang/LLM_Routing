import itertools
import math

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# City groups
groups = [
    [3, 8], [4, 13], [1, 2],
    [6, 14], [5, 9], [7, 12],
    [10, 11]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of cities taking one from each group
all_combinations = list(itertools.product(*groups))

# Function to calculate the route distance
def calculate_route_distance(route):
    total_distance = distance(0, route[0])  # Start from depot to first city in the route
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])  # Sum distances between consecutive cities
    total_distance += distance(route[-1], 0)  # Return to depot
    return total_distance

# Find the shortest route
shortest_tour = None
min_distance = float('inf')

for combination in all_combinations:
    route_distance = calculate_route_distance(combination)
    if route_distance < min_distance:
        min_distance = route_distance
        shortest_tour = combination

# Convert the shortest route to desired format (starting and ending at depot)
final_tour = [0] + list(shortest_tour) + [0]

# Output the result
print("Tour:", final_tour)
print("Total travel cost:", round(min_distance, 2))