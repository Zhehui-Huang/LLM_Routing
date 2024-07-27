import math
from itertools import product

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible route combinations
all_combinations = list(product(*groups))

def calculate_total_distance(route):
    total_distance = 0
    start_city = 0
    # Start and end at the depot
    path = [start_city] + list(route) + [start_city]
    for i in range(len(path) - 1):
        total_distance += distance(path[i], path[i+1])
    return total_distance, path

# Try all combinations and find the shortest tour
min_distance = float('inf')
best_tour = None

for combination in all_combinations:
    total_distance, tour_path = calculate_total_distance(combination)
    if total_distance < min_distance:
        min_distance = total_tour = total_distance
        best_tour = tour_path

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")