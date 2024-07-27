import math
import itertools

# Define the coordinates of cities
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1_index, city2_index):
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute all combinations of cities taking one from each group
city_combinations = list(itertools.product(*groups))

# Function to compute total tour distance for a sequence of city indices
def calculate_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour that visits one city from each group and returns to the depot
shortest_tour = None
shortest_tour_distance = float('inf')
depot = 0

for combination in city_combinations:
    tour = [depot] + list(combination) + [depot]  # tour starting and ending at the depot
    tour_distance = calculate_tour_distance(tour)
    if tour_distance < shortest_tour_distance:
        shortest_tour = tour
        shortest_tour_distance = tour_distance

# Output the shortest tour and its cost
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_tour_distance)