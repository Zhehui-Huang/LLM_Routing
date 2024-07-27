import itertools
import math

# City positions including the depot (city 0)
positions = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
             (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
             (53, 80), (21, 21), (12, 39)]

# Groups of cities
groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible group configurations where exactly one city is chosen per group
product_groups = list(itertools.product(*groups))

# Calculate the total distance for a given tour sequence
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

# Find the shortest possible tour by evaluating each combinations
min_distance = float('inf')
best_tour = None

for group_selection in product_groups:
    # We need to create permutations of the cities in the selected group configuration
    for perm in itertools.permutations(group_selection):
        # Constructing the tour starting and ending at the depot
        current_tour = [0] + list(perm) + [0]
        current_distance = calculate_tour_distance(current_tour)
        # Update if the current tour is better
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output the best tour and its total travel distance
print('Tour:', best_tour)
print('Total travel cost:', min_distance)