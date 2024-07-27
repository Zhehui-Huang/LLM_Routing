import itertools
import math

# City coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# City groups
groups = {
    0: [7, 9], 1: [1, 3], 2: [4, 6], 3: [8], 4: [5], 5: [2]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible combinations of cities (one from each group)
all_combinations = list(itertools.product(*groups.values()))

# Function to calculate the total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest tour
best_tour = None
best_cost = float('inf')
for combination in all_combinations:
    # Tours start and end at depot city 0
    current_tour = [0] + list(combination) + [0]
    current_cost = tour_client(current_tour)
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_tour

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)