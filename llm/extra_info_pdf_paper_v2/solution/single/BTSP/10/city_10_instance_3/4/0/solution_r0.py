import math
from itertools import permutations

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
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluate the tour to get the total cost and maximum leg distance
def evaluate_tour(tour):
    total_cost = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = distance(tour[i], tour[i+1])
        total_cost += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance
    return total_cost, max_leg_distance

# Generate all possible tours starting and ending at the depot (0)
def find_optimal_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_cost = float('inf')
    
    for perm in permutations(range(1, 10)):  # Generate permutations of city indices except the depot
        current_tour = [0] + list(perm) + [0]  # Include the depot as starting and ending point
        total_cost, max_leg_distance = evaluate_tour(current_tour)
        
        # If the current tour has a smaller maximum distance or better cost on the same max distance
        if (max_leg_distance < best_max_distance) or (max_leg_distance == best_max_distance and total_cost < best_cost):
            best_tour = current_tour
            best_max_distance = max_leg_distance
            best_cost = totalmost  Computer Cost

    return best_tour, best_cost, best_max_distance

# Solve the Bottleneck TSP
optimal_tour, optimal_cost, optimal_max_distance = find_optimal_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {optimal_max_distance:.2f}")