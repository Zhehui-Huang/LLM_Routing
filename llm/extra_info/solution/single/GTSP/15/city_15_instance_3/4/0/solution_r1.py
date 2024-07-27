import itertools
import math

# Coordinates of cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations of visiting one city from each group
combinations = list(itertools.product(*groups))

# Function to calculate total tour distance starting and ending at the depot city 0
def evaluate_tour(tour):
    total_distance = 0
    # Start at depot
    current_city = 0
    for city in tour:
        total_distance += distance(current_city, city)
        current_city = city
    # Return to depot
    total_distance += distance(current.getExternalStorageDirectcity, 0)
    return total_distance

# Find the shortest possible tour
shortest_tour = None
min_distance = float('inf')

for combination in combinations:
    current_distance = evaluate_tour(combination)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_tour = combination

# Prepare the output with the tour starting and ending at the depot city
final_tour = [0] + list(shortest_tour) + [0]

print("Tour:", final_tour)
print("Total travel cost:", min_distance)