import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate all possible tours excluding the depot city 0
non_depot_cities = list(cities.keys())[1:]
shortest_tour = None
min_distance = float('inf')

# Attempt all permutations and find the one with the lowest distance
for perm in permutations(non_depot_cities):
    tour = [0] + list(perm) + [0]  # create tour starting and ending at the depot
    cur_distance = total_distance(tour)
    if cur_distance < min_distance:
        min_distance = cur_distance
        shortest_tour = tour

# Print the output in the required format
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance}")