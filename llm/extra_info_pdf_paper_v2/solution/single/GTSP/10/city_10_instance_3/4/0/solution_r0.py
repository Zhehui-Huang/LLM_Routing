import math
import itertools

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Groups of cities
groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2],
}

# Calculates Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible combinations of one city from each group
group_combinations = list(itertools.product(*groups.values()))

# Function to calculate the total travel cost of a certain tour
def calculate_total_cost(tour):
    total_cost = calculate_distance(0, tour[0])  # Depot to first city
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    total_cost += calculate_distance(tour[-1], 0)  # Last city back to depot
    return total_cost

# Evaluate each combination of cities to find the one with the minimal travel cost
best_tour = None
best_cost = float('inf')

for tour in group_combinations:
    current_cost = calculate_total_cost(tour)
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = tour

# Return the result, including the depot city on both ends
final_tour = [0] + list(best_tour) + [0]
final_cost = best_cost

print("Tour:", final_tour)
print("Total travel cost:", final_cost)