import itertools
import math

# City and group definitions based on the problem statement
cities = {
    0: (9, 93),   # Depot
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating all possible tours that visit one city from each group
all_tours = itertools.product(groups[0], groups[1], groups[2])

# Finding the shortest possible tour
shortest_tour = None
min_distance = float('inf')

for tour in all_tours:
    # Always start and end at the depot (city 0)
    complete_tour = [0] + list(tour) + [0]
    total_distance = sum(calculate_distance(complete_tour[i], complete_tour[i+1]) for i in range(len(complete_tour) - 1))
    
    if total_distance < min_distance:
        min_distance = total_distance
        shortest_tour = complete_tour

# Printing the results correctly referring to the min_distance
print("Tour:", shortest_tour)
print("Total travel cost:", round(min_distance, 2))